Investigate a drop in the number of active users on your team's messaging app

How are the drops defined? fewer users today/this week?

Sudden vs Progressive drop?
Sudden -> bug, outage, data integrity, big event
Progressive -> industry trend, PR issue, seasonality

Drop across platform or just this product?

Which groups are affected?

Region?
If only 1 region, then network outage
Lack of understanding needs for these communities

User demographics (age, gender, race)?
Lack of understanding for those groups.

Platform (iOS, Android)?
If only one platform is affected, this could indicate bug or UI/UX issues

Theory 1: Functional bug preventing message to be sent
    Would expect to see # user start a message stay the same but completion decrease.
    Check: log clicks, check error logs

Theory 2: Data integrity
    Would expect there to be a sudden drop inconsistent with the previous and following day
    Check for incomplete data, check for faield etl pipelines

Theory 3: Cannibalization
    Would expect a consistent drop in messages but an uptick in usage of a competing product
    Identify new product launches and compare usage data

Theory 4: Seaonality
    Would expect a similar drop when compared to the previous year
    Compare data over multiple years and observe any patterns