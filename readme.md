This package takes in Land Registry data csv URLs, performs UX improvements, and sends the data to a MS SQL Server
<ol>
<li> Renames columns to user-friendly headers
<li> Renames the property type from S, D, etc to Semi, Detached, etc
<li> Breaks down the date column into day, month, year
<li> Breaks down the postcode column to post sector, area, region
</ol>
It then sends the data to a MS SQL Server.
<br>
See associated sample_dataset.csv for an example of the final output.