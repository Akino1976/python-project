Feature: common.utils

  Background:
    Given the module common.utils

  Scenario: offset_datetime_strftime(...) should return yesterday
    Given the parameters:
      format: "%Y-%m-%d"
      days: 1
    When I call the offset_datetime_strftime function
    Then the result should be !Ref yester_day_date
