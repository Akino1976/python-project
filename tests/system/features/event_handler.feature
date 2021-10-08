Feature: A call to run_jobs

  Scenario: Running the integration of invoicing for skane job export only preprocessing is True
    When I call the run_jobs.event_handler function
    Then the result should be !Ref yester_day_date
