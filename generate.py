"""
Generate corpus based on member id and limit of how many records we want
"""
from xml.dom import minidom
import pandas as pd
from pathlib import Path
import requests
import argparse
import os
from datetime import datetime


def get_age(date_of_birth, date_of_debate):
    birth_date = datetime.strptime(date_of_birth, "%Y-%m-%d")
    debate_date = datetime.strptime(date_of_debate, "%Y-%m-%d")
    age = debate_date.year - birth_date.year - ((debate_date.month, debate_date.day) < (birth_date.month, birth_date.day))
    return age


# Returns a list of dicts, each one representing a new record in our dataset
def parse_debate_XML(url, pId, name, date_of_birth, party, constituency):
    # Init pandas dataframe
    debate_data = pd.DataFrame(columns=['pId', 'date', 'housecode', 'houseno', 'date', 'topic', 'text', 'order'])
    debate_record = []

    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching data from API")
        return

    current_xml_debate_record = minidom.parseString(response.content)

    # Grab the house information from one of the metadata XML tags
    author_elements = current_xml_debate_record.getElementsByTagName('FRBRWork')[0].getElementsByTagName('FRBRauthor')[0]

    house = author_elements.getAttribute('href')
    housecode = Path(house).parts[-2]
    houseno = Path(house).parts[-1]

    # Grab the date
    date = current_xml_debate_record.getElementsByTagName('docDate')[0].getAttribute('date')

    # Calculate the age of the member at the time of this debate
    age = get_age(date_of_birth, date)

    # Cycle through debateSections
    debate_sections = current_xml_debate_record.getElementsByTagName('debateSection')
    for debate_section in debate_sections:

        # Grab debate section id
        debate_section_id = debate_section.attributes['eId'].value

        # Grab the topic
        headings = debate_section.getElementsByTagName('heading')
        for heading in headings:
            if heading.firstChild:  # Check if heading is non-empty
                topic = heading.firstChild.data
            else:
                topic = 'No topic'

        # Grab the TD's contribution as well as its order within the debate
        speeches = debate_section.getElementsByTagName('speech')
        for speech in speeches:
            contribution = ""
            if speech.attributes['by'].value == pId:  # e.g. '#EndaKenny'
                order = speech.attributes['eId'].value
                paragraphs = speech.getElementsByTagName('p')
                for paragraph in paragraphs:
                    if paragraph.firstChild and getattr(paragraph.firstChild, 'data', None):
                        contribution += paragraph.firstChild.data


                # Add entry to our debate data
                new_row = {
                    'name': name,
                    'age': age,
                    'party': party,
                    'constituency': constituency,
                    'pid': pId,
                    'date': date,
                    'house_code': housecode,
                    'house_no': houseno,
                    'debate_section_topic': topic,
                    'debate_section_id': debate_section_id,
                    'contribution': contribution,
                    'order_in_discourse': order
                }

                debate_record.append(new_row)

    return debate_record


def get_debate_records(member_id, limit):
    base_url = "https://api.oireachtas.ie/v1/debates"
    params = {
        "chamber_type": "house",
        "chamber": "dail",
        "date_start": "1900-01-01",
        "date_end": "2099-01-01",
        "member_id": f"https://data.oireachtas.ie/ie/oireachtas/member/id/{member_id}",
        "limit": limit
    }
    response = requests.get(base_url, params=params)

    if response.status_code != 200:
        print("Error fetching data from API")
        return

    json_response = response.json()

    xml_files = []
    results = json_response.get('results', [])
    for result in results:
        if 'debateRecord' not in result:
            continue
        formats = result['debateRecord'].get('formats', {})
        xml_uri = formats.get('xml', {}).get('uri')
        if xml_uri and xml_uri not in xml_files:
            xml_files.append(xml_uri)

    return xml_files


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fetch debate records.')
    parser.add_argument('member_uri', type=str, help='Member URI e.g. Enda-Kenny.D.1975-11-12')
    parser.add_argument('member_pId', type=str, help='Member pId e.g. \'#EndaKenny\'')
    parser.add_argument('member_name', type=str, help='Member name e.g. \'Enda Kenny\'')
    parser.add_argument('member_date_of_birth', type=str, help='Member date of birth e.g. Enda-Kenny.D.1951-04-21')
    parser.add_argument('member_party', type=str, help='Member party e.g. \'Fine Gael\'')
    parser.add_argument('member_constituency', type=str, help='Member constituency e.g. \'Mayo\'')
    parser.add_argument('limit', type=int,
                        help='Limit results (final no. of records could be lower after removing duplicates')

    args = parser.parse_args()

    debate_records = []

    xml_files = get_debate_records(args.member_uri, args.limit)
    for xml_file in xml_files:
        debate_record = parse_debate_XML(xml_file, args.member_pId, args.member_name, args.member_date_of_birth, args.member_party, args.member_constituency)
        debate_records.append(debate_record)

    flattened_debate_records = [item for sublist in debate_records for item in sublist]
    flattened_debate_records_df = pd.DataFrame(flattened_debate_records)

    if not os.path.exists("data"):
        os.makedirs("data")

    filename = f"data/{args.member_uri}_limit{args.limit}.tsv"
    flattened_debate_records_df.to_csv(filename, sep='\t', index=False)
    print(flattened_debate_records_df)
