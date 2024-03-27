### Background

A basic script to generate a tsv corpus of contributions from a particular member of oireachtas.

This approach searches debates by the member URI provided (for example, Enda-Kenny.D.1975-11-12), with the number of matches limited to the number provided (for example, 5000). This response contains debate records by section - excellent.

However, the XML files linked out to within the debate sections seem to be dead. Luckily, for each contribution we are also given a link out to the XML file for the entire day's debate (for example, https://data.oireachtas.ie/akn/ie/debateRecord/dail/2015-11-03/debate/mul@/main.xml).

So we build a list of unique XML files for all the days our wonderful member made contributions.

Within each of these XML files, we have enough information to glean the date, house code (for example, dail), house number (for example, 32 - the 32nd sitting of the Dáil), debate section topic (for example, 'Brexit Issues'), debate section id (for example, dbsect_37), contribution itself (we search for speech tags with the attribute by='#EndaKenny', or whatever our member's pId is), and the order of this contribution in the day's discourse (for example, spk_272 - the 272nd individual contribution of the day's debates).

### Usage

We need to pass memberUri, limit, and pId as arguments to the script.

`python generate.py 'Enda-Kenny.D.1975-11-12' '#EndaKenny' 'Enda Kenny' '1951-04-21' 'Fine Gael' 'Mayo' 5000`

Note that the memberUri and pId can be found by hitting the members endpoint for our desired oireachtas member over at https://api.oireachtas.ie/.

### Analysis

- File size `x-large` generated based on `limit10000`
- File size `large` generated based on `limit3000`
- File size `medium` generated based on `limit1000`
- File size `small` trimmed medium to first thousand lines in txt file. This has 732575 characters.

- We produce `formal-articles.txt` to have a similar character count of 744033.
- We produce `social-articles.txt` to have a similar character count of 