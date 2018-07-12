# Chi-Square Test of Independence

Perform a chi-square test to test independence of variables `LandSlope` and `SalePrice` in the IOWA housing dataset. `SalePrice` isn't a categorical variable, but we can divide it into three categories - High, medium, low using pandas qcut [function](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.qcut.html).

## Write a function `chi_square()` that
* Returns the p-value
* The Boolean result of Chi2-test

** Note - Use pandas qcut function to divide `SalePrice` into three equidistant categories - High, medium, low **

### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| df | DataFrame | compulsory |  | IOWA housing dataset |


### Returns:

| Return | dtype | description |
| --- | --- | --- |
| p_value | float | p-value |
| test_result | numpy.bool|result of our chi2-test(true or false) |
