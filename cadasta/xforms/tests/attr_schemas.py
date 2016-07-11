party_xform_group = {
    "label": "Party Attributes",
    "name": "party_attributes",
    "type": "group",
    "children": [
        {
            "label": "Gender",
            "name": "gender",
            "choices": [
                {
                    "label": "Male",
                    "name": "m"
                },
                {
                    "label": "Female",
                    "name": "f"
                }
            ],
            "default": "f",
            "bind": {
                "relevant": "${party_type}='individual'"
            },
            "type": "select one"
        },
        {
            "label": "Homeowner",
            "name": "homeowner",
            "hint": "Is homeowner",
            "choices": [
                {
                    "label": "Yes",
                    "name": "yes"
                },
                {
                    "label": "No",
                    "name": "no"
                }
            ],
            "default": "no",
            "bind": {
                "relevant": "${party_type}='individual'",
            },
            "type": "select one"
        },
        {
            "label": "Date of Birth",
            "name": "dob",
            "bind": {
                "relevant": "${party_type}='individual'",
                "required": "yes"
            },
            "type": "date"
        },
        {
            "label": "Notes",
            "name": "notes",
            "type": "text",
            "hint": "Additional Notes"
        }
    ],
}

location_xform_group = {
    "type": "group",
    "name": "location_attributes",
    "label": "Location Attributes",
    "children": [
        {
            "default": "none",
            "choices": [
                {
                    "name": "none",
                    "label": "No data"
                },
                {
                    "name": "text",
                    "label": "Textual"
                },
                {
                    "name": "point",
                    "label": "Point data"
                },
                {
                    "name": "polygon_low",
                    "label": "Low quality polygon"
                },
                {
                    "name": "polygon_high",
                    "label": "High quality polygon"
                }
            ],
            "hint": "Quality of parcel geometry",
            "name": "quality",
            "type": "select one",
            "label": "Spatial Unit Quality"
        },
        {
            "label": "Acquired when",
            "name": "acquired_when",
            "type": "date"
        },
        {
            "label": "Acquired how",
            "name": "acquired_how",
            "type": "select one",
            "choices": [
                {
                    "name": "CS",
                    "label": "Contractual Share Crop"
                },
                {
                    "name": "CA",
                    "label": "Customary Arrangement"
                },
                {
                    "name": "GF",
                    "label": "Gift"
                },
                {
                    "name": "HS",
                    "label": "Homestead"
                },
                {
                    "name": "IO",
                    "label": "Informal Occupant"
                },
                {
                    "name": "IN",
                    "label": "Inheritance"
                },
                {
                    "name": "LH",
                    "label": "Leasehold"
                },
                {
                    "name": "PF",
                    "label": "Purchased Freehold"
                },
                {
                    "name": "RN",
                    "label": "Rental"
                },
                {
                    "name": "OT",
                    "label": "Other"
                }
            ],
        },
        {
            "label": "Notes",
            "name": "notes",
            "type": "text",
            "hint": "Additional Notes"
        }
    ]
}

location_relationship_xform_group = {
    "name": "location_relationship_attributes",
    "children": [
        {
            "name": "notes",
            "label": "Notes",
            "type": "text"
        }
    ],
    "label": "Location relationship attributes",
    "type": "group"
}

party_relationship_xform_group = {
    "name": "party_relationship_attributes",
    "children": [
        {
            "name": "notes",
            "label": "Notes",
            "type": "text"
        }
    ],
    "label": "Party relationship attributes",
    "type": "group"
}

tenure_relationship_xform_group = {
    "name": "tenure_relationship_attributes",
    "children": [
        {
            "label": "Notes",
            "name": "notes",
            "type": "text",
            "hint": "Additional Notes"
        }
    ],
    "label": "Tenure relationship attributes",
    "type": "group"
}
