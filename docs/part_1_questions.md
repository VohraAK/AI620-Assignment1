### Part 1 Questions:

---

#### a) **Data Heterogeneity**: Explain how your chosen data sources represent different data types (structured, semi-structured, unstructured). Provide concrete examples from your extracted data.

##### **Answer**: 

The WB_FINDEX dataset is inherently structured, since the authors have defined a strict tabular schema with explicitly typed columns. Data is extracted in CSV format with 10 columns, each column has a specific data type (integral, categorcal)

*Example (first 2 rows from WB_FINDEX)*:

```csv
STRUCTURE,STRUCTURE_ID,ACTION,FREQ,REF_AREA,INDICATOR,SEX,AGE,URBANISATION,UNIT_MEASURE,COMP_BREAKDOWN_1,COMP_BREAKDOWN_2,COMP_BREAKDOWN_3,TIME_PERIOD,UNIT_TYPE,DATABASE_ID,TIME_FORMAT,UNIT_MULT,DATA_SOURCE,OBS_CONF,OBS_VALUE,OBS_STATUS,FREQ_LABEL,REF_AREA_LABEL,INDICATOR_LABEL,SEX_LABEL,AGE_LABEL,URBANISATION_LABEL,UNIT_MEASURE_LABEL,COMP_BREAKDOWN_1_LABEL,COMP_BREAKDOWN_2_LABEL,COMP_BREAKDOWN_3_LABEL,UNIT_TYPE_LABEL,DATABASE_ID_LABEL,TIME_FORMAT_LABEL,UNIT_MULT_LABEL,OBS_STATUS_LABEL,DATA_SOURCE_LABEL,OBS_CONF_LABEL
datastructure,WB.DATA360:DS_DATA360(1.3),I,A3,ZMB,WB_FINDEX_FH1_FH2,_T,Y_GE15,RUR,PT_RESP,_T,_T,_T,2024,RATIO,WB_FINDEX,602,0,WB_FINDEX,PU,63.962716537911604,A,Triennial,Zambia,Sent or received domestic remittances,Total,15 years old and over,Rural area,Percentage of respondents,Total,Total,Total,Ratio,Global Findex Database,CCYY,Units,Normal value,Global Findex Database,Public
datastructure,WB.DATA360:DS_DATA360(1.3),I,A3,ZMB,WB_FINDEX_FH1_FH2,_T,Y_GE15,URB,PT_RESP,_T,_T,_T,2024,RATIO,WB_FINDEX,602,0,WB_FINDEX,PU,69.99341827219871,A,Triennial,Zambia,Sent or received domestic remittances,Total,15 years old and over,Urban area,Percentage of respondents,Total,Total,Total,Ratio,Global Findex Database,CCYY,Units,Normal value,Global Findex Database,Public
```

<br>

Data extracted from Google Trends is also structured, but it is simpler in terms of schema:

```csv
date,JazzCash,EasyPaisa,SadaPay,NayaPay,Raast,isPartial
2021-02-07,21,42,1,0,1,False
2021-02-14,20,43,1,0,0,False
```
The sturcture is not as rigid as `WB_FINDEX`, but it still is structured in a readable, indexable format.


Data from the NewsAPI source is a JSON response object dump, which, after some processing, boils down to an array of objects mainly containing unstructured textual data. This can be classified as unstructured.


---

#### (b) **Extraction Challenges:** Discuss specific technical or practical challenges encountered while accessing different data sources (rate limits, authentication, data format inconsistencies, etc.).

##### **Answer**:

While I did not encounter issues with rate limits, authentication, etc, I did find it really challenging to work with NewsAPI, especially since it was not extracting news articles relevant to my specific keywords; often times, it would extract completely unrelated articles, or some articles which might have contained partials of these specific keywords. This was the main reason why I could not further process, tranasform and visualise the extracted news articles.

---

#### (c) Storage Justification: Explain why storing data in multiple formats (CSV, JSON) is valuable in a data engineering context. When would you choose one format over another?

##### **Answer**:
CSVs are inherently structured into a tabluar format (rows x columns), so they are positioned to be better in indexing, searching and filtering for data. They work well with databases, making them ideal for structured datasets.

JSON is best for representing hierarchical and nested data structures, making it perfect for APIs and config files. It preserves the original data schema using key-value pairs, which works well for semi-structured data like news articles with specific metadata.
