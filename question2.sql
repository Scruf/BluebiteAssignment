SELECT campaigns.id , campaigns.name
FROM campaigns
	INNER JOIN venue_types ON
		venue_types.id = tags.venue_type_id
	INNER JOIN tags ON
		tags.id = campaign_tag.tag_id
	INNER JOIN campaigns ON
		campaigns.id = campaign_tag.campaign_id