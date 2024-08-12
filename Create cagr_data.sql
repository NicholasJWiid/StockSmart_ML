CREATE TABLE CAGR_data (
    ticker VARCHAR(10) PRIMARY KEY,
    stock_name VARCHAR(100) NOT NULL,
    headquarters VARCHAR(100),
    cagr_2023 FLOAT,
    cagr_2022 FLOAT,
	cagr_2021 FLOAT,
	cagr_2020 FLOAT,
	cagr_2019 FLOAT,
	cagr_2018 FLOAT,
	cagr_2017 FLOAT,
	cagr_2016 FLOAT,
	cagr_2015 FLOAT
);
