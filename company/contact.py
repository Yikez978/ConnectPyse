class Contact(object):
    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.firstName = None  # *(String(30))
        self.lastName = None  # (String(30))
        self.type = None  # (ContactTypeReference)
        self.company = None  # (CompanyReference)
        self.site = None  # (SiteReference)
        self.addressLine1 = None  # (String(50))
        self.addressLine2 = None  # (String(50))
        self.city = None  # (String(50))
        self.state = None  # (String(50))
        self.zip = None  # (String(12))
        self.country = None  # (String(50))
        self.relationship = None  # (RelationshipReference)
        self.department = None  # (ContactDepartmentReference)
        self.inactiveFlag = None  # (Boolean)
        self.defaultMergeContactId = None  # (Integer)
        self.securityIdentifier = None  # (String(184))
        self.managerContactId = None  # (Integer)
        self.assistantContactId = None  # (Integer)
        self.title = None  # (String(100))
        self.school = None  # (String(50))
        self.nickName = None  # (String(30))
        self.marriedFlag = None  # (Boolean)
        self.childrenFlag = None  # (Boolean)
        self.significantOther = None  # (String(30))
        self.portalPassword = None  # (String(15))
        self.portalSecurityLevel = None  # (Integer)
        self.disablePortalLoginFlag = None  # (Boolean)
        self.unsubscribeFlag = None  # (Boolean)
        self.gender = None  # (Enum)
        self.birthDay = None  # (String)
        self.anniversary = None  # (String)
        self.presence = None  # (Enum)
        self.mobileGuid = None  # (Guid)
        self.facebookUrl = None  # (String)
        self.twitterUrl = None  # (String)
        self.linkedInUrl = None  # (String)
        self.defaultBillingFlag = None  # (Boolean)
        self.communicationItems = None  # (Array)
        self._info = None  # (Metadata)
        self.customFields = None  # (Array)

        # initialize object with json dict
        self.__dict__.update(json_dict)

    def __repr__(self):
        string = ''
        for k, v in self.__dict__.items():
            string = ''.join([string, '{}: {}\n'.format(k, v)])
        return string