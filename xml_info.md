### Note that the XML file is of the following schema:

```
<akomaNtoso xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://docs.oasis-open.org/legaldocml/ns/akn/3.0/CSD13" xsi:schemaLocation="http://docs.oasis-open.org/legaldocml/ns/akn/3.0/CSD13 ./akomantoso30.xsd">
<debate name="Official Report">
<meta>
...
</meta>
<preface>
...
</preface>
<debateBody>
...
</debateBody>
</debate>
</akomaNtoso>
```

---

### Note that in XML, each debateSection looks like the following:

```
<debateSection name="question" eId="dbsect_11">
    <heading>
        Cabinet Committee Meetings
        <recordedTime time="2016-11-23T13:10:00+00:00"/>
    </heading>
    <question by="#MichaelMartin" to="#Taoiseach" eId="pq_4">
    ...
    </question>
    <question by="#MickBarry" to="#Taoiseach" eId="pq_5">
    ...
    </question>
    <question by="#GerryAdams" to="#Taoiseach" eId="pq_6">
    ...
    </question>
    <question by="#JoanBurtonLAB" to="#Taoiseach" eId="pq_7">
    ...
    </question>
    <speech by="#EndaKenny" eId="spk_122">
    ...
    </speech>
    <speech by="#MichaelMartin" eId="spk_123">
    ...
    </speech>
    <speech by="#MickBarry" eId="spk_124">
    ...
    </speech>
    <speech by="#GerryAdams" eId="spk_125">
    ...
    </speech>
    <speech by="#MichaelMartin" eId="spk_126">
    ...
    </speech>
    <speech by="#GerryAdams" eId="spk_127">
    ...
    </speech>
    <speech by="#JoanBurtonLAB" eId="spk_128">
    ...
    </speech>
    <speech by="#EndaKenny" eId="spk_129">
    ...
    </speech>
    <speech by="#JoanBurtonLAB" eId="spk_130">
    ...
    </speech>
    <speech by="#SeanOFearghaillFF" eId="spk_131">
    ...
    </speech>
    <speech by="#RichardBoydBarrett" eId="spk_132">
    ...
    </speech>
    <speech by="#SeanOFearghaillFF" eId="spk_133">
    ...
    </speech>
    <speech by="#GerryAdams" eId="spk_134">
    ...
    </speech>
    <speech by="#SeanOFearghaillFF" eId="spk_135">
    ...
    </speech>
    <speech by="#BridSmith" eId="spk_136">
    ...
    </speech>
    <speech by="#RichardBoydBarrett" eId="spk_137">
    ...
    </speech>
    <speech by="#SeanOFearghaillFF" eId="spk_138">
    ...
    </speech>
    <speech by="#BridSmith" eId="spk_139">
    ...
    </speech>
    <speech by="#JoanBurtonLAB" eId="spk_140">
    ...
    </speech>
    <speech by="#BridSmith" eId="spk_141">
    ...
    </speech>
    <speech by="#MichaelMartin" eId="spk_142">
    ...
    </speech>
    <speech by="#SeanOFearghaillFF" eId="spk_143">
    ...
    </speech>
    <speech by="#EndaKenny" eId="spk_144">
    ...
    </speech>
    <speech by="#MichaelMartin" eId="spk_145">
    ...
    </speech>
    <speech by="#EndaKenny" eId="spk_146">
    ...
    </speech>
    <speech by="#JoanBurtonLAB" eId="spk_147">
    ...
    </speech>
    <speech by="#EndaKenny" eId="spk_148">
    ...
    </speech>
    <speech by="#JoanBurtonLAB" eId="spk_149">
    ...
    </speech>
    <speech by="#EndaKenny" eId="spk_150">
    ...
    </speech>
    <speech by="#SeanOFearghaillFF" eId="spk_151">
    ...
    </speech>
</debateSection>
```

---

### So in each XML file, we want:

```
akomaNtoso
    debate
        meta
            identification
                FRBRWork
                    <FRBRauthor as="#author" href="/ie/oireachtas/house/dail/32"/> - gives us house
        preface
            <block name="date_en">
                <docDate date="2016-11-23">Wednesday, 23 November 2016</docDate> - gives us date
            </block>
        debateBody
            <debateSection name="billReport" refersTo="#bill.2016.83.dail.4" eId="dbsect_2"> - gives us section of daily debate this is found in
                <heading>
                    Finance Bill 2016: Report Stage (Resumed) - gives us topic
                    <recordedTime time="2016-11-23T10:00:00+00:00"/>
                </heading>
                <speech by="#MichaelNoonan" as="#Minister_for_Finance" eId="spk_1"> - gives us text and cardinal order
                    <p eId="para_1">I move amendment No. 6:</p>
                    <p class="indent_1" eId="para_2">In page 7, line 36, to delete “Schedule E.” and substitute “Schedule E.”.”.</p>
                    <p eId="para_3">This is a technical amendment which corrects a minor error in the Bill which resulted from the acceptance on Committee Stage of an amendment from Deputy Michael McGrath. It reinserts necessary punctuation that had been inadvertently deleted when the end date of the tax credit was removed.</p>
                </speech>

Getting the speeches is more difficult.
Each speech tag could contain many sub tags like <from> or otherwise.
All we need to do is concatenate all the <p> tags into one blob, then save this as an entry.
(There are also question tags filled with <b> (bold) sub-tags. But feel like we can ignore these.)
```