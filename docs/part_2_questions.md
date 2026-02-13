### Part 2 Questions:

---

#### a) Cleaning Rationale: Justify your data cleaning decisions. Why were specific approaches chosen for handling missing data or outliers?

##### **Answer**:
For all of my extracted datasets, I had made seperate sandboxed walkthroughs of their section of the pipeline, which showed that they all had no missing data or duplicated rows.

For `WB_FINDEX` data, I filtered out data for Pakistan, spliced out unneeded columns (most columns had a `_LABEL` version which was more informative than the numerical/categorical version of the feature). In the end, I had 98 rows of Pakistani data concentrated around specific indicators:

```python
FINDEX_KEY_INDICATORS = ["Made or received a digital payment", "Made a digital merchant payment", "Received digital payments", "Mobile money account", "Digitally enabled account", "Used mobile phone or card to pay for in-store purchase", "Used a mobile phone or the internet to pay bills", "Used a mobile phone or the internet to buy something online", "Received wages: through a mobile phone", "Made a utility payment: using a mobile phone"]
```
<br>

For Google Trends, I removed the `isPartial` column as it was `False` for all datapoints, thus serving no purpose. The monthly timestamps required conversion to `datetime` format for time-series analysis. Each trends category was saved as a separate CSV for category-separation and to make it easier to work woth. 

---

#### (b) Visualization Insights: What key insights or patterns emerge from your visualizations? How do they relate to your chosen thematic domain?

##### **Answer**:

![alt text](/docs/wb_findex_15_to_24.png)
![alt text](/docs/wb_findex_wallet_keyword_trends.png)


From these visualisations:
- `JazzCash` and `EasyPaisa` remain the topdogs in terms of most-searched-for mobile/digital wallets in Pakistan, with their popularity steadily increasing as the techonology is democratized and becoming more accessible.
- Around a quarter of Pakistan's 15-24 year old population has made or created a digital account, with more than 15% of the demographic having access to a mobile money account. This shows how the young population in Pakistan is also moving towards digital payment solutions as these techologies become easier to use.

---

#### (c) Visualization Critique: What limitations exist in your current visualizations? How could they be improved for different audiences (technical vs. business stakeholders)?

##### **Answer:**

![alt text](/docs/wb_findex_wallet_keyword_trends.png)

- The trendlines for `SadaPay`, `NayaPay`, and `Raast` are overlapping, making their trends hard to see. 

<br>

![alt text](/docs/wb_findex_15_to_24.png)

- This histogram only compares the percentage values for indicators of a specific demographic; it would be nicer to do a comparitive analysis **across time-periods (2021 v.s. 2024, e.t.c)**. This would aid business stakeholders in making informed predictions about payment-wallet adoption rates in Pakistan. 

- There should be exact percentage points on each bar of the histogram plot; this makes data easier to visualise and read, both for the techinical and the business audience.