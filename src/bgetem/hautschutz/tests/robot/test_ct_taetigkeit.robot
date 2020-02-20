# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s bgetem.hautschutz -t test_taetigkeit.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src bgetem.hautschutz.testing.BGETEM_HAUTSCHUTZ_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/bgetem/hautschutz/tests/robot/test_taetigkeit.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Taetigkeit
  Given a logged-in site administrator
    and an add Taetigkeit form
   When I type 'My Taetigkeit' into the title field
    and I submit the form
   Then a Taetigkeit with the title 'My Taetigkeit' has been created

Scenario: As a site administrator I can view a Taetigkeit
  Given a logged-in site administrator
    and a Taetigkeit 'My Taetigkeit'
   When I go to the Taetigkeit view
   Then I can see the Taetigkeit title 'My Taetigkeit'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Taetigkeit form
  Go To  ${PLONE_URL}/++add++Taetigkeit

a Taetigkeit 'My Taetigkeit'
  Create content  type=Taetigkeit  id=my-taetigkeit  title=My Taetigkeit

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Taetigkeit view
  Go To  ${PLONE_URL}/my-taetigkeit
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Taetigkeit with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Taetigkeit title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
