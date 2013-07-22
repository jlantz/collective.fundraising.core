*** Settings ***

Library  Selenium2Library  timeout=10  implicit_wait=0.5 
Library  OperatingSystem

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/variables.robot
Resource  plone/app/robotframework/keywords.robot
Resource  plone/app/robotframework/server.robot
Resource  collective/fundraising/core/tests/keywords.robot

Suite Setup  Start browser
Suite Teardown  Close All Browsers

*** Test Cases ***

Fundraising Settings fields store values
    [tags]  Fundraising Settings
    Wait until page contains  Plone
    Login as site owner

    Create dexterity type  Test Fundraising Settings  test_fundraising_settings
    Enable behavior  Fundraising Settings

    Go to homepage
    Open Add New Menu
    Click link  xpath=//a/span[contains(., "Test Fundraising Settings")]/..
    Wait until page contains  Add Test Fundraising Settings

    Input text  form-widgets-IDublinCore-title  Test Organization Settings
    Populate Fundraising Settings field  org_name  Test Organization
    Populate Fundraising Settings field  ask_levels  5|5,10,25,50
    Populate Fundraising Settings field  ask_level  5
    Populate Fundraising Settings field  goal  100
    Populate Fundraising Settings field  ask_quantities  1|1,2,3,4,5
    Populate Fundraising Settings field  ask_quantity  1
    Select Fundraising Settings checkbox  allow_pf
    Populate Fundraising Settings field  completion_threshold  25
    Populate Fundraising Settings field  pf_completion_threshold  10
    Click Button  Save

    Click Edit in edit bar
    Fundraising Settings value should be  org_name  Test Organization
#    Fundraising Settings value should be  ask_levels  5|5,10,25,50
    Fundraising Settings value should be  ask_level  5
    Fundraising Settings value should be  goal  100
#    Fundraising Settings value should be  ask_quantities  1|1,2,3,4,5
    Fundraising Settings value should be  ask_quantity  1
    Fundraising Settings checkbox should be selected  allow_pf
    Fundraising Settings value should be  completion_threshold  25
    Fundraising Settings value should be  pf_completion_threshold  10
    
    Populate Fundraising Settings field  completion_threshold  15
    Populate Fundraising Settings field  pf_completion_threshold  5
    Click Button  Save

    Click Edit in edit bar
    Fundraising Settings value should be  completion_threshold  15
    Fundraising Settings value should be  pf_completion_threshold  5

Fundraising Campaign fields store values
    [tags]  Fundraising Campaign

    Wait until page contains  Plone
    Login as site owner

    Create dexterity type  Test Fundraising Campaign  test_fundraising_campaign
    Enable behavior  Fundraising Campaign

    Go to homepage
    Open Add New Menu
    Click link  xpath=//a/span[contains(., "Test Fundraising Campaign")]/..
    Wait until page contains  Add Test Fundraising Campaign

    Input text  form-widgets-IDublinCore-title  Test Fundraising Campaign
    Populate Fundraising Campaign field  goal  110
    Select Fundraising Campaign checkbox  allow_pf
    Click Button  Save

    Click Edit in edit bar
    Fundraising Campaign value should be  goal  110
    Fundraising Campaign checkbox should be selected  allow_pf
    Populate Fundraising Campaign field  goal  210
    Click Button  Save

    Click Edit in edit bar
    Fundraising Campaign value should be  goal  210
    Click Button  Save

Fundraising Page field store values
    [tags]  Fundraising Page

    Wait until page contains  Plone
    Login as site owner

    Create dexterity type  Test Fundraising Page  test_fundraising_page
    Enable behavior  Fundraising Page

    Go to homepage
    Open Add New Menu
    Click link  xpath=//a/span[contains(., "Test Fundraising Page")]/..
    Wait until page contains  Add Test Fundraising Page

    Input text  form-widgets-IDublinCore-title  Test Fundraising Page
    Populate Fundraising Page field  goal  120
    Click Button  Save

    Click Edit in edit bar
    Fundraising Page value should be  goal  120
    Populate Fundraising Page field  goal  220
    Click Button  Save

    Click Edit in edit bar
    Fundraising Page value should be  goal  220

Personal Fundraiser field stores values
    [tags]  Personal Fundraiser

    Wait until page contains  Plone
    Login as site owner

    Create dexterity type  Test Personal Fundraiser  test_fundraising_page
    Enable behavior  Personal Fundraiser

    Go to homepage
    Open Add New Menu
    Click link  xpath=//a/span[contains(., "Test Personal Fundraiser")]/..
    Wait until page contains  Add Test Personal Fundraiser

    Input text  form-widgets-IDublinCore-title  Test Personal Fundraiser
    Populate Personal Fundraiser field  pf_goal  130
    Click Button  Save

    Click Edit in edit bar
    Personal Fundraiser value should be  pf_goal  130
    Populate Personal Fundraiser field  pf_goal  230
    Click Button  Save

    Click Edit in edit bar
    Personal Fundraiser value should be  pf_goal  230

Personal Fundraiser can combine with page, campaign, and settings
    [tags]  Personal Fundraiser  Fundraising Page  Fundraising Campaign  Fundraising Settings
    Wait until page contains  Plone
    Login as site owner

    Create dexterity type  Test Combo  test_combo
    Enable behavior  Fundraising Settings
    Enable behavior  Fundraising Campaign
    Enable behavior  Fundraising Page
    Enable behavior  Personal Fundraiser

    Go to homepage
    Open Add New Menu
    Click link  xpath=//a/span[contains(., "Test Combo")]/..
    Wait until page contains  Add Test Combo

    Input text  form-widgets-IDublinCore-title  Test Combo 

    Populate Fundraising Settings field  org_name  Test Organization
    Populate Fundraising Settings field  ask_levels  5|5,10,25,50
    Populate Fundraising Settings field  ask_level  5
    Populate Fundraising Settings field  goal  100
    Populate Fundraising Settings field  ask_quantities  1|1,2,3,4,5
    Populate Fundraising Settings field  ask_quantity  1
    Select Fundraising Settings checkbox  allow_pf
    Populate Fundraising Settings field  completion_threshold  25
    Populate Fundraising Settings field  pf_completion_threshold  10
    Populate Fundraising Campaign field  goal  110
    Select Fundraising Campaign checkbox  allow_pf
    Populate Fundraising Page field  goal  120
    Populate Personal Fundraiser field  pf_goal  130
    Click Button  Save

    Click Edit in edit bar
    Fundraising Settings value should be  org_name  Test Organization
#    Fundraising Settings value should be  ask_levels  5|5,10,25,50
    Fundraising Settings value should be  ask_level  5
    Fundraising Settings value should be  goal  100
#    Fundraising Settings value should be  ask_quantities  1|1,2,3,4,5
    Fundraising Settings value should be  ask_quantity  1
    Fundraising Settings checkbox should be selected  allow_pf
    Fundraising Settings value should be  completion_threshold  25
    Fundraising Settings value should be  pf_completion_threshold  10
    Fundraising Campaign value should be  goal  110
    Fundraising Campaign checkbox should be selected  allow_pf
    Fundraising Page value should be  goal  120
    Personal Fundraiser value should be  pf_goal  130

    Populate Fundraising Settings field  goal  200
    Populate Fundraising Campaign field  goal  210
    Populate Fundraising Page field  goal  220
    Populate Personal Fundraiser field  pf_goal  230
    Click Button  Save

    Click Edit in edit bar
    Fundraising Settings value should be  goal  200
    Fundraising Campaign value should be  goal  210
    Fundraising Page value should be  goal  220
    Personal Fundraiser value should be  pf_goal  230


Fundraising Campaign inherits default values from Fundraising Settings
    [tags]  Inheritance  Fundraising Campaign  Fundraising Settings
    Wait until page contains  Plone
    Login as site owner

    Create dexterity type  Test Settings  test_settings
    Enable behavior  Fundraising Settings
    Create dexterity type  Test Campaign  test_campaign
    Enable behavior  Fundraising Campaign

    Go to homepage
    Open Add New Menu
    Click link  xpath=//a/span[contains(., "Test Settings")]/..
    Wait until page contains  Add Test Settings

    Input text  form-widgets-IDublinCore-title  Test Settings 
    Populate Fundraising Settings field  org_name  Test Organization
    Populate Fundraising Settings field  goal  100
    Select Fundraising Settings checkbox  allow_pf
    Click Button  Save

    Open Add New Menu
    Click link  xpath=//a/span[contains(., "Test Campaign")]/..
    Input text  form-widgets-IDublinCore-title  Test Campaign
    Click Button  Save

    Click Edit in edit bar
    Fundraising Campaign value should be  goal  100
    Click Button  Cancel

    Go to  ${PLONE_URL}/test-settings
    Click Edit in edit bar
    Fundraising Settings value should be  goal  100
    Populate Fundraising Settings field  goal  200
    Click Button  Save

    Go to  ${PLONE_URL}/test-settings/test-campaign
    Click Edit in edit bar
    Fundraising Campaign value should be  goal  200
    Populate Fundraising Campaign field  goal  300
    Click Button  Save

    Go to  ${PLONE_URL}/test-settings
    Click Edit in edit bar
    Populate Fundraising Settings field  goal  400
    Click Button  Save

    Go to  ${PLONE_URL}/test-settings/test-campaign
    Click Edit in edit bar
    Fundraising Campaign value should be  goal  300
    Click Button  Cancel
    

Fundraising Page inherits default values from Fundraising Campaign and Fundraising Settings
    [tags]  Inheritance  Fundraising Page  Fundraising Campaign  Fundraising Settings
    Wait until page contains  Plone
    Login as site owner

    Create dexterity type  Test Settings  test_settings
    Enable behavior  Fundraising Settings
    Create dexterity type  Test Campaign  test_campaign
    Enable behavior  Fundraising Campaign
    Create dexterity type  Test Page  test_page
    Enable behavior  Fundraising Page

    Go to homepage
    Open Add New Menu
    Click link  xpath=//a/span[contains(., "Test Settings")]/..
    Wait until page contains  Add Test Settings

    Input text  form-widgets-IDublinCore-title  Test Settings 
    Populate Fundraising Settings field  org_name  Test Organization
    Populate Fundraising Settings field  goal  100
    Select Fundraising Settings checkbox  allow_pf
    Click Button  Save

    Open Add New Menu
    Click link  xpath=//a/span[contains(., "Test Campaign")]/..
    Input text  form-widgets-IDublinCore-title  Test Campaign
    Click Button  Save

    Open Add New Menu
    Click link  xpath=//a/span[contains(., "Test Page")]/..
    Input text  form-widgets-IDublinCore-title  Test Page
    Click Button  Save

    Click Edit in edit bar
    Fundraising Page value should be  goal  100
    Click Button  Cancel
    
    Go to  ${PLONE_URL}/test-settings
    Click Edit in edit bar
    Fundraising Settings value should be  goal  100
    Populate Fundraising Settings field  goal   200
    Click Button  Save

    Go to  ${PLONE_URL}/test-settings/test-campaign/test-page
    Click Edit in edit bar
    Fundraising Page value should be  goal  200
    Click Button  Cancel

    Go to  ${PLONE_URL}/test-settings/test-campaign
    Click Edit in edit bar
    Populate Fundraising Campaign field  goal  110
    Click Button  Save

    Go to  ${PLONE_URL}/test-settings/test-campaign/test-page
    Click Edit in edit bar
    Fundraising Page value should be  goal  110
    Populate Fundraising Page field  goal  120
    Click Button  Save

    Click Edit in edit bar
    Fundraising Page value should be  goal  120
    Click Button  Cancel


Personal Fundraiser inherits default values from Fundraising Campaign and Fundraising Settings
    [tags]  Inheritance  Personal Fundraiser  Fundraising Campaign  Fundraising Settings
    Wait until page contains  Plone
    Login as site owner

    Create dexterity type  Test Settings  test_settings
    Enable behavior  Fundraising Settings
    Create dexterity type  Test Campaign  test_campaign
    Enable behavior  Fundraising Campaign
    Create dexterity type  Test Personal  test_personal
    Enable behavior  Personal Fundraiser

    Go to homepage
    Open Add New Menu
    Click link  xpath=//a/span[contains(., "Test Settings")]/..
    Wait until page contains  Add Test Settings

    Input text  form-widgets-IDublinCore-title  Test Settings 
    Populate Fundraising Settings field  org_name  Test Organization
    Populate Fundraising Settings field  pf_goal  100
    Select Fundraising Settings checkbox  allow_pf
    Click Button  Save

    Open Add New Menu
    Click link  xpath=//a/span[contains(., "Test Campaign")]/..
    Input text  form-widgets-IDublinCore-title  Test Campaign
    Click Button  Save

    Open Add New Menu
    Click link  xpath=//a/span[contains(., "Test Personal")]/..
    Input text  form-widgets-IDublinCore-title  Test Personal
    Click Button  Save

    Click Edit in edit bar
    Personal Fundraiser value should be  pf_goal  100
    Click Button  Cancel
    
    Go to  ${PLONE_URL}/test-settings
    Click Edit in edit bar
    Fundraising Settings value should be  pf_goal  100
    Populate Fundraising Settings field  pf_goal   200
    Click Button  Save

    Go to  ${PLONE_URL}/test-settings/test-campaign/test-personal
    Click Edit in edit bar
    Personal Fundraiser value should be  pf_goal  200
    Click Button  Cancel

    Go to  ${PLONE_URL}/test-settings/test-campaign
    Click Edit in edit bar
    Populate Fundraising Campaign field  pf_goal  110
    Click Button  Save

    Go to  ${PLONE_URL}/test-settings/test-campaign/test-personal
    Click Edit in edit bar
    Personal Fundraiser value should be  pf_goal  110
    Populate Personal Fundraiser field  pf_goal  120
    Click Button  Save

    Click Edit in edit bar
    Personal Fundraiser value should be  pf_goal  120
    Click Button  Cancel

