#!/usr/bin/env python


def compute_fund(num_of_year: int, yearly_investment: int, yearly_interest_ratio: float, start_year: int,
                 start_fund: int):
    current_fund = start_fund
    for year in range(start_year, start_year + num_of_year):
        print(f'{year}: {current_fund}')
        current_fund = current_fund * (1 + yearly_interest_ratio) + yearly_investment


if __name__ == "__main__":
    start_year = 2021
    start_fund = 200000
    yearly_investment = 200000
    yearly_interest_ratio = 0.3
    num_of_year = 20
    compute_fund(num_of_year, yearly_investment, yearly_interest_ratio, start_year, start_fund)
