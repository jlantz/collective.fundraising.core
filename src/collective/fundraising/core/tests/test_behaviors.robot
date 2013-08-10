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

Fundraising Organization fields store values
    [tags]  Fundraising Organization
    Wait until page contains  Plone
    Login as site owner

    Create dexterity type  Test Fundraising Organization  test_fundraising_organization
    Enable behavior  Fundraising Organization

    Go to homepage
    Open Add New Menu
    Click link  xpath=//a/span[contains(., "Test Fundraising Organization")]/..
    Wait until page contains  Add Test Fundraising Organization

    Input text  form-widgets-IDublinCore-title  Test Organization Organization
    Populate Fundraising Organization field  org_name  Test Organization
    Populate Fundraising Organization field  ask_levels  5|5,10,25,50
    Populate Fundraising Organization field  ask_level  5
    Populate Fundraising Organization field  goal  100
    Populate Fundraising Organization field  ask_quantities  1|1,2,3,4,5
    Populate Fundraising Organization field  ask_quantity  1
    Select Fundraising Organization checkbox  allow_pf
    Populate Fundraising Organization field  completion_threshold  25
    Populate Fundraising Organization field  pf_completion_threshold  10
    Click button  Save

    Click Edit in edit bar
    Fundraising Organization value should be  org_name  Test Organization
#    Fundraising Organization value should be  ask_levels  5|5,10,25,50
    Fundraising Organization value should be  ask_level  5
    Fundraising Organization value should be  goal  100
#    Fundraising Organization value should be  ask_quantities  1|1,2,3,4,5
    Fundraising Organization value should be  ask_quantity  1
    Fundraising Organization checkbox should be selected  allow_pf
    Fundraising Organization value should be  completion_threshold  25
    Fundraising Organization value should be  pf_completion_threshold  10
    
    Populate Fundraising Organization field  completion_threshold  15
    Populate Fundraising Organization field  pf_completion_threshold  5
    Click button  Save

    Click Edit in edit bar
    Fundraising Organization value should be  completion_threshold  15
    Fundraising Organization value should be  pf_completion_threshold  5

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
    Click button  Save

    Click Edit in edit bar
    Fundraising Campaign value should be  goal  110
    Fundraising Campaign checkbox should be selected  allow_pf
    Populate Fundraising Campaign field  goal  210
    Click button  Save

    Click Edit in edit bar
    Fundraising Campaign value should be  goal  210
    Click button  Save

Fundraising Page fields store values
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
    Click button  Save

    Click Edit in edit bar
    Fundraising Page value should be  goal  120
    Populate Fundraising Page field  goal  220
    Click button  Save

    Click Edit in edit bar
    Fundraising Page value should be  goal  220

Personal Fundraiser fields store values
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
    Populate Personal Fundraiser field  first_name  James
    Populate Personal Fundraiser field  last_name  Madison
    Populate Personal Fundraiser field  pf_goal  130
    Click button  Save

    Click Edit in edit bar
    Personal Fundraiser value should be  first_name  James
    Personal Fundraiser value should be  last_name  Madison
    Personal Fundraiser value should be  pf_goal  130
    Populate Personal Fundraiser field  pf_goal  230
    Click button  Save

    Click Edit in edit bar
    Personal Fundraiser value should be  pf_goal  230

Donor fields store values
    [tags]  Donor

    Wait until page contains  Plone
    Login as site owner

    Create dexterity type  Test Donor  test_donor
    Enable behavior  Donor

    Go to homepage
    Open Add New Menu
    Click link  xpath=//a/span[contains(., "Test Donor")]/..
    Wait until page contains  Add Test Donor

    Input text  form-widgets-IDublinCore-title  Test Donor
    Populate Donor field  first_name  John
    Click button  Save

    Click Edit in edit bar
    Donor value should be  first_name  John
    Populate Donor field  first_name  Jane
    Click button  Save

    Click Edit in edit bar
    Donor value should be  first_name  Jane

Donation fields store values
    [tags]  Donor

    Wait until page contains  Plone
    Login as site owner

    Create dexterity type  Test Donation  test_donation
    Enable behavior  Donation

    Go to homepage
    Open Add New Menu
    Click link  xpath=//a/span[contains(., "Test Donation")]/..
    Wait until page contains  Add Test Donation

    Input text  form-widgets-IDublinCore-title  Test Donation
    Populate Donation field  amount  100
    Click button  Save

    Click Edit in edit bar
    Donation value should be  amount  100.0
    Populate Donation field  amount  110
    Click button  Save

    Click Edit in edit bar
    Donation value should be  amount  110.0

Dedication fields store values
    [tags]  Dedication

    Wait until page contains  Plone
    Login as site owner

    Create dexterity type  Test Dedication  test_dedication
    Enable behavior  Dedication

    Go to homepage
    Open Add New Menu
    Click link  xpath=//a/span[contains(., "Test Dedication")]/..
    Wait until page contains  Add Test Dedication

    Input text  form-widgets-IDublinCore-title  Test Dedication
    Populate Dedication field  dedication_type  honorary
    Click button  Save

    Click Edit in edit bar
    Dedication value should be  dedication_type  honorary 
    Populate Dedication field  dedication_type  memorial
    Click button  Save

    Click Edit in edit bar
    Dedication value should be  dedication_type  memorial

Personal Fundraiser can combine with page, campaign, and organization
    [tags]  Personal Fundraiser  Fundraising Page  Fundraising Campaign  Fundraising Organization
    Wait until page contains  Plone
    Login as site owner

    Create dexterity type  Test Combo  test_combo
    Enable behavior  Fundraising Organization
    Enable behavior  Fundraising Campaign
    Enable behavior  Fundraising Page
    Enable behavior  Personal Fundraiser

    Go to homepage
    Open Add New Menu
    Click link  xpath=//a/span[contains(., "Test Combo")]/..
    Wait until page contains  Add Test Combo

    Input text  form-widgets-IDublinCore-title  Test Combo 

    Populate Fundraising Organization field  org_name  Test Organization
    Populate Fundraising Organization field  ask_levels  5|5,10,25,50
    Populate Fundraising Organization field  ask_level  5
    Populate Fundraising Organization field  goal  100
    Populate Fundraising Organization field  ask_quantities  1|1,2,3,4,5
    Populate Fundraising Organization field  ask_quantity  1
    Select Fundraising Organization checkbox  allow_pf
    Populate Fundraising Organization field  completion_threshold  25
    Populate Fundraising Organization field  pf_completion_threshold  10
    Populate Fundraising Campaign field  goal  110
    Select Fundraising Campaign checkbox  allow_pf
    Populate Fundraising Page field  goal  120
    Populate Personal Fundraiser field  first_name  James
    Populate Personal Fundraiser field  last_name  Madison
    Populate Personal Fundraiser field  pf_goal  130
    Click button  Save

    Click Edit in edit bar
    Fundraising Organization value should be  org_name  Test Organization
#    Fundraising Organization value should be  ask_levels  5|5,10,25,50
    Fundraising Organization value should be  ask_level  5
    Fundraising Organization value should be  goal  100
#    Fundraising Organization value should be  ask_quantities  1|1,2,3,4,5
    Fundraising Organization value should be  ask_quantity  1
    Fundraising Organization checkbox should be selected  allow_pf
    Fundraising Organization value should be  completion_threshold  25
    Fundraising Organization value should be  pf_completion_threshold  10
    Fundraising Campaign value should be  goal  110
    Fundraising Campaign checkbox should be selected  allow_pf
    Fundraising Page value should be  goal  120
    Personal Fundraiser value should be  first_name  James
    Personal Fundraiser value should be  last_name  Madison
    Personal Fundraiser value should be  pf_goal  130

    Populate Fundraising Organization field  goal  200
    Populate Fundraising Campaign field  goal  210
    Populate Fundraising Page field  goal  220
    Populate Personal Fundraiser field  pf_goal  230
    Click button  Save

    Click Edit in edit bar
    Fundraising Organization value should be  goal  200
    Fundraising Campaign value should be  goal  210
    Fundraising Page value should be  goal  220
    Personal Fundraiser value should be  pf_goal  230

Donor can combine with Donation and Dedication
    [tags]  Donor  Donation  Dedication
    Wait until page contains  Plone
    Login as site owner

    Create dexterity type  Test Donation Combo  test_donation_combo
    Enable behavior  Donor
    Enable behavior  Donation
    Enable behavior  Dedication

    Go to homepage
    Open Add New Menu
    Click link  xpath=//a/span[contains(., "Test Donation Combo")]/..
    Wait until page contains  Add Test Donation Combo

    Input text  form-widgets-IDublinCore-title  Test Donation Combo 
    Populate Donor field  first_name  John
    Populate Donation field  amount  100
    Populate Dedication field  first_name  Jack
    Click button  Save

    Click Edit in edit bar
    Donor value should be  first_name  John
    Donation value should be  amount  100.0
    Dedication value should be  first_name  Jack
    Populate Donor field  first_name  Jane
    Populate Donation field  amount  110
    Populate Dedication field  first_name  Jill
    Click button  Save

    Click Edit in edit bar
    Donor value should be  first_name  Jane
    Donation value should be  amount  110.0
    Dedication value should be  first_name  Jill

Fundraising Campaign inherits default values from Fundraising Organization
    [tags]  Inheritance  Fundraising Campaign  Fundraising Organization
    Wait until page contains  Plone
    Login as site owner

    Create dexterity type  Test Organization  test_organization
    Enable behavior  Fundraising Organization
    Create dexterity type  Test Campaign  test_campaign
    Enable behavior  Fundraising Campaign

    Go to homepage
    Open Add New Menu
    Click link  xpath=//a/span[contains(., "Test Organization")]/..
    Wait until page contains  Add Test Organization

    Input text  form-widgets-IDublinCore-title  Test Organization 
    Populate Fundraising Organization field  org_name  Test Organization
    Populate Fundraising Organization field  goal  100
    Select Fundraising Organization checkbox  allow_pf
    Click button  Save

    Open Add New Menu
    Click link  xpath=//a/span[contains(., "Test Campaign")]/..
    Input text  form-widgets-IDublinCore-title  Test Campaign
    Click button  Save

    Click Edit in edit bar
    Fundraising Campaign value should be  goal  100
    Click button  Cancel

    Go to  ${PLONE_URL}/test-organization
    Click Edit in edit bar
    Fundraising Organization value should be  goal  100
    Populate Fundraising Organization field  goal  200
    Click button  Save

    Go to  ${PLONE_URL}/test-organization/test-campaign
    Click Edit in edit bar
    Fundraising Campaign value should be  goal  200
    Populate Fundraising Campaign field  goal  300
    Click button  Save

    Go to  ${PLONE_URL}/test-organization
    Click Edit in edit bar
    Populate Fundraising Organization field  goal  400
    Click button  Save

    Go to  ${PLONE_URL}/test-organization/test-campaign
    Click Edit in edit bar
    Fundraising Campaign value should be  goal  300
    Click button  Cancel
    

Fundraising Page inherits default values from Fundraising Campaign and Fundraising Organization
    [tags]  Inheritance  Fundraising Page  Fundraising Campaign  Fundraising Organization
    Wait until page contains  Plone
    Login as site owner

    Create dexterity type  Test Organization  test_organization
    Enable behavior  Fundraising Organization
    Create dexterity type  Test Campaign  test_campaign
    Enable behavior  Fundraising Campaign
    Create dexterity type  Test Page  test_page
    Enable behavior  Fundraising Page

    Go to homepage
    Open Add New Menu
    Click link  xpath=//a/span[contains(., "Test Organization")]/..
    Wait until page contains  Add Test Organization

    Input text  form-widgets-IDublinCore-title  Test Organization 
    Populate Fundraising Organization field  org_name  Test Organization
    Populate Fundraising Organization field  goal  100
    Select Fundraising Organization checkbox  allow_pf
    Click button  Save

    Open Add New Menu
    Click link  xpath=//a/span[contains(., "Test Campaign")]/..
    Input text  form-widgets-IDublinCore-title  Test Campaign
    Click button  Save

    click Edit in edit bar
    Fundraising Campaign value should be  goal  100
    click button  Save

    Open Add New Menu
    Click link  xpath=//a/span[contains(., "Test Page")]/..
    Input text  form-widgets-IDublinCore-title  Test Page
    Click button  Save

    Click Edit in edit bar
    Fundraising Page value should be  goal  100
    Click button  Cancel
    
    Go to  ${PLONE_URL}/test-organization
    Click Edit in edit bar
    Fundraising Organization value should be  goal  100
    Populate Fundraising Organization field  goal   200
    Click button  Save

    Go to  ${PLONE_URL}/test-organization/test-campaign/test-page
    Click Edit in edit bar
    Fundraising Page value should be  goal  200
    Click button  Cancel

    Go to  ${PLONE_URL}/test-organization/test-campaign
    Click Edit in edit bar
    Populate Fundraising Campaign field  goal  110
    Click button  Save

    Go to  ${PLONE_URL}/test-organization/test-campaign/test-page
    Click Edit in edit bar
    Fundraising Page value should be  goal  110
    Populate Fundraising Page field  goal  120
    Click button  Save

    Click Edit in edit bar
    Fundraising Page value should be  goal  120
    Click button  Cancel


Personal Fundraiser inherits default values from Fundraising Campaign and Fundraising Organization
    [tags]  Inheritance  Personal Fundraiser  Fundraising Campaign  Fundraising Organization
    Wait until page contains  Plone
    Login as site owner

    Create dexterity type  Test Organization  test_organization
    Enable behavior  Fundraising Organization
    Create dexterity type  Test Campaign  test_campaign
    Enable behavior  Fundraising Campaign
    Create dexterity type  Test Personal  test_personal
    Enable behavior  Personal Fundraiser

    Go to homepage
    Open Add New Menu
    Click link  xpath=//a/span[contains(., "Test Organization")]/..
    Wait until page contains  Add Test Organization

    Input text  form-widgets-IDublinCore-title  Test Organization 
    Populate Fundraising Organization field  org_name  Test Organization
    Populate Fundraising Organization field  pf_goal  100
    Select Fundraising Organization checkbox  allow_pf
    Click button  Save

    Open Add New Menu
    Click link  xpath=//a/span[contains(., "Test Campaign")]/..
    Input text  form-widgets-IDublinCore-title  Test Campaign
    Click button  Save

    Open Add New Menu
    Click link  xpath=//a/span[contains(., "Test Personal")]/..
    Input text  form-widgets-IDublinCore-title  Test Personal
    Populate Personal Fundraiser field  first_name  James
    Populate Personal Fundraiser field  last_name  Madison
    Click button  Save

    Click Edit in edit bar
    Personal Fundraiser value should be  first_name  James
    Personal Fundraiser value should be  last_name  Madison
    Personal Fundraiser value should be  pf_goal  100
    Click button  Cancel
    
    Go to  ${PLONE_URL}/test-organization
    Click Edit in edit bar
    Fundraising Organization value should be  pf_goal  100
    Populate Fundraising Organization field  pf_goal   200
    Click button  Save

    Go to  ${PLONE_URL}/test-organization/test-campaign/test-personal
    Click Edit in edit bar
    Personal Fundraiser value should be  pf_goal  200
    Click button  Cancel

    Go to  ${PLONE_URL}/test-organization/test-campaign
    Click Edit in edit bar
    Populate Fundraising Campaign field  pf_goal  110
    Click button  Save

    Go to  ${PLONE_URL}/test-organization/test-campaign/test-personal
    Click Edit in edit bar
    Personal Fundraiser value should be  pf_goal  110
    Populate Personal Fundraiser field  pf_goal  120
    Click button  Save

    Click Edit in edit bar
    Personal Fundraiser value should be  pf_goal  120
    Click button  Cancel

