# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s bgetem.hautschutz -t test_hautschutzmittel.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src bgetem.hautschutz.testing.BGETEM_HAUTSCHUTZ_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/bgetem/hautschutz/tests/robot/test_hautschutzmittel.robot
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

Scenario: As a site administrator I can add a Hautschutzmittel
  Given a logged-in site administrator
    and an add Hautschutzmittel form
   When I type 'My Hautschutzmittel' into the title field
    and I submit the form
   Then a Hautschutzmittel with the title 'My Hautschutzmittel' has been created

Scenario: As a site administrator I can view a Hautschutzmittel
  Given a logged-in site administrator
    and a Hautschutzmittel 'My Hautschutzmittel'
   When I go to the Hautschutzmittel view
   Then I can see the Hautschutzmittel title 'My Hautschutzmittel'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Hautschutzmittel form
  Go To  ${PLONE_URL}/++add++Hautschutzmittel

a Hautschutzmittel 'My Hautschutzmittel'
  Create content  type=Hautschutzmittel  id=my-hautschutzmittel  title=My Hautschutzmittel

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Hautschutzmittel view
  Go To  ${PLONE_URL}/my-hautschutzmittel
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Hautschutzmittel with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Hautschutzmittel title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
