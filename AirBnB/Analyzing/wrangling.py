import re
import numpy as np
import pandas as pd

# from combine import df
from combine_all import df

# Austin Tx Listings
df.address = df.address.apply(lambda x: 'Austin, Texas' if 'Texas' in x else x)
df.address = df.address.apply(lambda x: 'Austin, Texas' if 'Austin' in x else x)

# NWA listings
df.address = df.address.apply(lambda x: 'Fayetteville' if 'Prairie Grove' in x else x)
df.address = df.address.apply(lambda x: 'Fayetteville' if 'Fayetteville' in x else x)
df.address = df.address.apply(lambda x: 'Fayetteville' if 'Farm' in x else x)

df.address = df.address.apply(lambda x: 'Rogers' if 'Rogers' in x else x)
df.address = df.address.apply(lambda x: 'Rogers' if 'Lowell' in x else x)


df.address = df.address.apply(lambda x: 'Bentonville' if 'Bentonville' in x else x)
df.address = df.address.apply(lambda x: 'Bentonville' if 'Centerton' in x else x)
df.address = df.address.apply(lambda x: 'Bentonville' if 'Pea Ridge' in x else x)
df.address = df.address.apply(lambda x: 'Bentonville' if 'Bentonville' in x else x)

df.address = df.address.apply(lambda x: 'Springdale' if 'Tonti' in x else x)
df.address = df.address.apply(lambda x: 'Springdale' if 'Springdale' in x else x)

df.address = df.address.apply(lambda x: 'Bella Vista' if 'Bella Vista' in x else x)
df.address = df.address.apply(lambda x: 'Bella Vista' if 'Pineville' in x else x)

# Central Ar listings
df.address = df.address.apply(lambda x: 'Hot Springs' if 'Hot Springs' in x else x)
df.address = df.address.apply(lambda x: 'Hot Springs' if 'Cave' in x else x)
df.address = df.address.apply(lambda x: 'Hot Springs' if 'Lake' in x else x)
df.address = df.address.apply(lambda x: 'Hot Springs' if 'Garland' in x else x)
df.address = df.address.apply(lambda x: 'Hot Springs' if 'Piney' in x else x)
df.address = df.address.apply(lambda x: 'Hot Springs' if 'Alex' in x else x)
df.address = df.address.apply(lambda x: 'Hot Springs' if 'Royal' in x else x)
df.address = df.address.apply(lambda x: 'Hot Springs' if 'Whittington' in x else x)
df.address = df.address.apply(lambda x: 'Hot Springs' if 'Rockwell' in x else x)
df.address = df.address.apply(lambda x: 'Hot Springs' if 'Arkansas, United States' in x else x)


df.address = df.address.apply(lambda x: 'Little Rock' if 'Little Rock' in x else x)
df.address = df.address.apply(lambda x: 'Little Rock' if 'Sherwood' in x else x)

cols_to_drop_temp = [
    'city',
    "calendar",
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

df = df.drop(cols_to_drop_temp, axis=1)

df['bedroomLabel'] = df['bedroomLabel'].replace('Studio', '0 bedrooms')
df['bedroomLabel'] = df['bedroomLabel'].replace('', '0 bedrooms')
new = df["bathroomLabel"].str.split(" ", n=1, expand=True)
df["rooms"] = new[0]

df = df[df['url'] != 'https://www.airbnb.com/rooms/35002301']
df = df[df['url'] != 'https://www.airbnb.com/rooms/52169286']
df = df[df['url'] != 'https://www.airbnb.com/rooms/42738847']
df = df[df['bedLabel'] != '61 beds']
df = df[df['bedLabel'] != '132 beds']
df = df[df['bathroomLabel'] != '']

new1 = df["bedLabel"].str.split(" ", n=1, expand=True)
new1 = new1.replace('', '0')
df["beds"] = new1[0]

new = df["bathroomLabel"].str.split(" ", n=1, expand=True)
df['baths'] = new[0].astype(float)
df.columns = [re.sub("[ ,\$]", "_", re.sub("[.]", "", c)) for c in df.columns]

dropme = ['name', 'country', 'listingRooms', 'roomType',
          'bedroomLabel', 'bedLabel', 'bathroomLabel',
          'seeAllAmenitySections', 'categorizedPreviewAmenities',
          'reviewsModulelocalizedOverallRating',
          'priceDetails', 'photos',
          'amenities_selectListViewPhoto', 'amenities_selectTileViewPhoto',
          'listingAmenities','amenities_description',  'reviews', 'url', 'guestControlspersonCapacity'
          ]

df = df.drop(dropme, axis=1)

df = df.rename(
    columns={
        'reviewDetailsInterfacereviewCount': 'reviewCount',
        'isHostedBySuperhost': 'Superhost',
        'roomTypeCategory': 'listingType',
        'pricingrateamount': 'pricepernight', 
    }
)

df.Superhost = df.Superhost.astype(np.int64)

df = df.reindex(
    columns=[
        'pricepernight', 'address', 'listingType', 'stars', 'reviewCount','id', 'Superhost',
        'minNights', 'maxNights','numberOfGuests', 'rooms', 'beds', 'baths', 'locationlat',
        'locationlng', 'amenities_id', 'amenities_isPresent', 'amenities_name',
        'guestControlsallowsChildren',	'guestControlsallowsEvents', 'guestControlsallowsInfants',
        'guestControlsallowsPets',	'guestControlsallowsSmoking',	
       
    ]
)

df.listingType.value_counts(normalize=True)
df = pd.get_dummies(df, columns=['amenities_name'])
df.columns = [re.sub("[ ,\$]", "_", re.sub("[.]", "", c)) for c in df.columns]
df = df[df.amenities_isPresent != False]
df = df.drop(columns=["amenities_isPresent", "amenities_id"])

df['rooms'] = df['rooms'].astype(float)
df['beds'] = df['beds'].astype(float)

id_group = df.groupby(['id'])
df = id_group.max()
df = df[df['pricepernight'].notna()]

mean_value=df['stars'].mean()
df.stars.fillna(value=mean_value, inplace=True)


transformed_df = pd.get_dummies(df)
df = pd.get_dummies(df, columns=['address','listingType'])
df.columns = [re.sub("[ ,\$]", "_", re.sub("[.]", "", c)) for c in df.columns]

df.columns = df.columns.str.replace('guestControlsallows', '')
df.columns = df.columns.str.replace('amenities_name_', '')
df.columns = df.columns.str.replace("Children’s", 'Children')
df.columns = df.columns.str.replace("Pack_’n_play/", 'Children')


df.to_csv('airbnb_data_cleaned.csv')
# target='pricepernight'
# used_cols = [c for c in df.columns.tolist() if c not in [target]]
# X=df[used_cols]
# y=df[target]

