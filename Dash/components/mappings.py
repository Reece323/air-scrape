import json
import re
import urllib.request

import folium
import pandas as pd

url = 'https://raw.githubusercontent.com/Reece323/air-scrape/main/Data/Bentonville_all.json'
response = urllib.request.urlopen(url)
Bentonville = json.loads(response.read())
Bville = pd.json_normalize(Bentonville)

cols_to_drop_temp = [
    # 'url',
    "calendar",
    'rootAmenitySections',
    'p3SummaryAddress',
    'primaryHost.about',
    'primaryHost.badges',
    'primaryHost.firstName',
    'primaryHost.id',
    'primaryHost.isSuperhost',
    'primaryHost.memberSinceFullStr',
    'primaryHost.name',
    'primaryHost.languages',
    'primaryHost.pictureUrl',
    'primaryHost.responseRateWithoutNa',
    'primaryHost.responseTimeWithoutNa',
    'primaryHost.hasInclusionBadge',
    'primaryHost.pictureLargeUrl',
    'primaryHost.hostIntroTags',
    'primaryHost.hostUrl',
    'primaryHost.listingsCount',
    'primaryHost.totalListingsCount',
    'tierId',
    'hasSpecialOffer',
    'hasWeWorkLocation',
    'hasWeWorkLocation',
    'additionalHosts',
    'hometourRooms',
    'hometourSections',
    'descriptionLocale',
    'initialDescriptionAuthorType',
    'localizedCheckInTimeWindow',
    'localizedCheckOutTime',
    'hometourRooms',
    'countryCode',
    'hasHostGuidebook',
    'hasLocalAttractions',
    'neighborhoodCommunityTags',
    'state',
    'paidGrowthRemarketingListingIds',
    'hasCommercialHostInfo',
    'hostSignatureFont.url',
    'nearbyAirportDistanceDescriptions',
    'propertyTypeInCity',
    'renderTierId',
    'isHotel',
    'isNewListing',
    'showReviewTag',
    'isRepresentativeInventory',
    'localizedCity',
    'highlights',
    'highlightsImpressionId',
    'pointOfInterests',
    'hostGuidebook.guidebookUrl',
    'hostGuidebook.localizedNameForHomesPdp',
    'hostGuidebook.title',
    'hostGuidebook.id',
    'pageViewType',
    'previewTags',
    'seeAllHometourSections',
    'enableHighlightsVoting',
    'heroModule.categorizedPhotos',
    'sortedReviews',
    'documentDisplayPictures',
    'sections',
    'p3ImpressionId',
    'paidGrowthRemarketingListingIdsStr',
    'isBusinessTravelReady',
    'address',
    'hasHouseRules',
    'reviewsOrder',
    'hostQuote',
    'localizedListingExpectations',
    'pricing.rate.amount_formatted',
    'pricing.rate.currency',
    'pricing.rate.is_micros_accuracy',
    'pricing.rate_with_service_fee.amount_formatted',
    'pricing.rate_with_service_fee.currency',
    'pricing.rate_with_service_fee.is_micros_accuracy',
    'reviewDetailsInterface.reviewSummary',
    'reviewsModule.appreciationTags',
    'pricing.rate_with_service_fee.amount',
    'pricing.rate_type',
    'sectionedDescription.authorType',
    'sectionedDescription.locale',
    'sectionedDescription.localizedLanguageName',
    'sectionedDescription.notes',
    'sectionedDescription.space',
    'guestControls.allowsNonChinaUsers',
    'guestControls.structuredHouseRulesWithTips',
    'sectionedDescription.neighborhoodOverview',
    'sectionedDescription.access',
    'sectionedDescription.description',
    'sectionedDescription.interaction',
    'sectionedDescription.name',
    'sectionedDescription.summary',
    'sectionedDescription.transit',
    # 'name',
    'listingExpectations',
    'sectionedDescription.houseRules',
    'additionalHouseRules',
    'idStr'
]

Bville = Bville.drop(cols_to_drop_temp, axis=1)

df = Bville.reindex(columns=[
    'url',
    'name',
    'city',
    'country',
    'id',
    'location.lat',
    'location.lng',
    'numberOfGuests',
    'listingRooms',
    'roomType',
    'roomTypeCategory',
    'bedroomLabel',
    'bedLabel',
    'bathroomLabel',
    'listingAmenities',
    'seeAllAmenitySections',
    'categorizedPreviewAmenities',
    'stars',
    'reviewsModule.localizedOverallRating',
    'reviewDetailsInterface.reviewCount',
    'reviews',
    'isHostedBySuperhost',
    'maxNights',
    'minNights',
    'priceDetails',
    'pricing.rate.amount',
    'guestControls.allowsChildren',
    'guestControls.allowsEvents',
    'guestControls.allowsInfants',
    'guestControls.allowsPets',
    'guestControls.allowsSmoking',
    'guestControls.personCapacity',
    'photos',
    'guestControls.structuredHouseRules',
]
)

df.columns = [re.sub("[ ,\$]", "_", re.sub("[.]", "", c)) for c in df.columns]
# print(df.columns)
df

df.columns = [re.sub("[ ,\$]", "_", re.sub("[.]", "", c)) for c in df.columns]


columns_to_split = ['bedroomLabel', 'bedLabel', 'bathroomLabel']


df['geometry'] = [(xy) for xy in zip(df.locationlat, df.locationlng)]

df

# print(fg)
colors = [
    'red',
    'blue',
    'gray',
    'darkred',
    'lightred',
    'orange',
    'beige',
    'green',
    'darkgreen',
    'lightgreen',
    'darkblue',
    'lightblue',
    'purple',
    'darkpurple',
    'pink',
    'cadetblue',
    'lightgray',
    'black'
]


