
""" Definition

Identification:
http://www.usccb.org/about/anti-trafficking-program/identifying-trafficking-victims.cfm
https://polarisproject.org/recognize-signs

Resources:
http://humantrafficking.unc.edu/resources/

"""

# Common Work and Living Conditions: The individual(s) in question

HT_NO_FREEDOM = 'HT_NO_FREEDOM'       # Is not free to leave or come and go as he/she wishes
HT_UNDER_18 = 'HT_UNDER_18'           # Is under 18 and is providing commercial sex acts
HT_COMMERCIAL_PIMP = 'HT_COMMERCIAL_PIMP'  # Is in the commercial sex industry and has a pimp / manager
HT_LOW_PAID = 'HT_LOW_PAID'        # Is unpaid, paid very little, or paid only through tips
HT_UNUSUAL_WORKTIME = 'HT_UNUSUAL_WORKTIME' # Works excessively long and/or unusual hours
HT_NO_BREAK = 'HT_NO_BREAK'         # Is not allowed breaks or suffers under unusual restrictions at work
HT_OWE_DEBT = 'HT_OWE_DEBT'         # Owes a large debt and is unable to pay it off
HT_FALSE_PROMISE = 'HT_FALSE_PROMISE'    # Was recruited through false promises concerning the nature and conditions of his/her work
HT_HIGH_SECURITY_MEASURE = 'HT_HIGH_SECURITY_MEASURE' # High security measures exist in the work and/or living locations (e.g. opaque windows, boarded up windows, bars on windows, barbed wire, security cameras, etc.)

# Poor Mental Health or Abnormal Behavior
"""
Is fearful, anxious, depressed, submissive, tense, or nervous/paranoid
Exhibits unusually fearful or anxious behavior after bringing up law enforcement
Avoids eye contact

"""
HT_POOR_MHNAB = 'HT_POOR_MHNAB'      # Poor Mental Health or Abnormal Behavior

# Lack of Control
"""
Has few or no personal possessions
Is not in control of his/her own money, no financial records, or bank account
Is not in control of his/her own identification documents (ID or passport)
Is not allowed or able to speak for themselves (a third party may insist on being present and/or translating)
"""
HT_LACK_OF_CONTROL = 'HT_LACK_OF_CONTROL'


# OTHERS
"""
Claims of just visiting and inability to clarify where he/she is staying/address
Lack of knowledge of whereabouts and/or do not know what city he/she is in
Loss of sense of time
Has numerous inconsistencies in his/her story
"""
HT_INA_LOCATION = 'HT_INA_LOCATION'
HT_INA_TIME = 'HT_INA_TIME'
HT_INCONSISTENCY = 'HT_INCONSISTENCY'


# DESCRIPTION
# http://adjectivesstarting.com/adjectives-to-describe-a-person/

HT_DESC_NATIONALITY = 'HT_DESC_NATIONALITY'   # Nationality is the nation or country to which someone belongs to. 
HT_DESC_PHSICAL_APPEARANCE = 'HT_DESC_PHSICAL_APPEARANCE'          # Physical appearance is self-explanatory.
HT_DESC_PERSONALITY = 'HT_DESC_PERSONALITY'   # Personality means an individual's tendencies to behave, think, and react in a particular way. 
HT_DESC_STYLE = 'HT_DESC_STYLE'         # A person's style is really their way of dressing, and the way they carry themselves.
HT_DESC_CHAR_TRAIT = 'HT_DESC_CHAR_TRAIT'    # Characteristics and Traits


# ACTION

HT_ACT_SERVICE_VISIT = 'HT_ACT_SERVICE_VISIT'  # girl visit
HT_ACT_SERVICE_UNPAID = 'HT_ACT_SERVICE_UNPAID' # unpaid service
HT_ACT_SERVICE_AFTER = 'HT_ACT_SERVICE_AFTER'  # action after service

HT_ACT_SEX_GROUP = 'HT_ACT_SEX_GROUP'      # group sex, more than one man and woman
HT_ACT_SEX_POSITION = 'HT_ACT_SEX_POSITION'

HT_ACT_FIND = 'HT_ACT_FIND'           # the way to find this




HT_LABELS = [
                HT_NO_FREEDOM,
                HT_UNDER_18,
                HT_COMMERCIAL_PIMP,
                HT_LOW_PAID,
                HT_UNUSUAL_WORKTIME,
                HT_NO_BREAK,
                HT_OWE_DEBT,
                HT_FALSE_PROMISE,
                HT_HIGH_SECURITY_MEASURE,
                HT_POOR_MHNAB,
                HT_LACK_OF_CONTROL,
                HT_INA_LOCATION,
                HT_INA_TIME,
                HT_INCONSISTENCY,
                HT_DESC_NATIONALITY,
                HT_DESC_PHSICAL_APPEARANCE,
                HT_DESC_PERSONALITY,
                HT_DESC_STYLE,
                HT_DESC_CHAR_TRAIT,
                HT_ACT_SERVICE_VISIT,
                HT_ACT_SERVICE_UNPAID,
                HT_ACT_SERVICE_AFTER,
                HT_ACT_SEX_GROUP,
                HT_ACT_SEX_POSITION,
                HT_ACT_FIND
            ]

# print HT_LABELS
