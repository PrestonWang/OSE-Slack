class selectCategory:
    """Constructs the onboarding message and stores the state of which tasks were completed."""
 [
	{
		"type": "section",
		"block_id": "Club Category",
		"text": {
			"type": "mrkdwn",
			"text": "Please select which category your organization belongs to"
		},
		"accessory": {
			"action_id": "Club Category",
			"type": "multi_static_select",
			"placeholder": {
				"type": "plain_text",
				"text": "Select items"
			},
			"options": [
				{
					"text": {
						"type": "plain_text",
						"text": "Academic"
					},
					"value": "Academic"
				},
				{
					"text": {
						"type": "plain_text",
						"text": "Arts"
					},
					"value": "Arts"
				},
				{
					"text": {
						"type": "plain_text",
						"text": "Athletic/Recreational"
					},
					"value": "Athletic/Recreational"
				},
				{
					"text": {
						"type": "plain_text",
						"text": "Community Service"
					},
					"value": "Community Service"
				},
				{
					"text": {
						"type": "plain_text",
						"text": "Cultural"
					},
					"value": "Cultural"
				},
                {
					"text": {
						"type": "plain_text",
						"text": "Dance"
					},
					"value": "Dance"
				},
				{
					"text": {
						"type": "plain_text",
						"text": "Pre-Professional"
					},
					"value": "Pre-Professional"
				},
				{
					"text": {
						"type": "plain_text",
						"text": "Religious"
					},
					"value": "Religious"
				},
				{
					"text": {
						"type": "plain_text",
						"text": "Social"
					},
					"value": "Social"
				},
				{
					"text": {
						"type": "plain_text",
						"text": "Social Awareness/Political"
					},
					"value": "Social Awareness/Political"
				}
			]
		}
	}
]