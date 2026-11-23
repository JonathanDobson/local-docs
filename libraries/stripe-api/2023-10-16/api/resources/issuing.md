# Stripe API 2023-10-16 — issuing

Operations under `/v1/issuing` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/issuing/authorizations

operationId: `GetIssuingAuthorizations`

Returns a list of Issuing `Authorization` objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `card` | string |  | Only return authorizations that belong to the given card. |
| `cardholder` | string |  | Only return authorizations that belong to the given cardholder. |
| `created` | object or integer |  | Only return authorizations that were created during the given date interval. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `status` | enum: `closed`, `pending`, `reversed` |  | Only return authorizations with the given status. One of `pending`, `closed`, or `reversed`. |

Returns: object

## GET /v1/issuing/authorizations/{authorization}

operationId: `GetIssuingAuthorizationsAuthorization`

Retrieves an Issuing `Authorization` object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `authorization (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `issuing.authorization`

## POST /v1/issuing/authorizations/{authorization}

operationId: `PostIssuingAuthorizationsAuthorization`

Updates the specified Issuing `Authorization` object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `authorization (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |

Returns: `issuing.authorization`

## POST /v1/issuing/authorizations/{authorization}/approve

operationId: `PostIssuingAuthorizationsAuthorizationApprove`

**Deprecated.**

[Deprecated] Approves a pending Issuing `Authorization` object. This request should be made within the timeout window of the [real-time authorization](https://stripe.com/docs/issuing/controls/real-time-authorizations) flow. 
This method is deprecated. Instead, [respond directly to the webhook request to approve an authorization](https://stripe.com/docs/issuing/controls/real-time-authorizations#authorization-handling).

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `authorization (path)` | string | yes |  |
| `amount` | integer |  | If the authorization's `pending_request.is_amount_controllable` property is `true`, you may provide this value to control how much to hold for the authorization. Must be positive (use [`decline`](https://stripe.com/docs/api/issuing/authorizations/decline) to decline an authorization request). |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |

Returns: `issuing.authorization`

## POST /v1/issuing/authorizations/{authorization}/decline

operationId: `PostIssuingAuthorizationsAuthorizationDecline`

**Deprecated.**

[Deprecated] Declines a pending Issuing `Authorization` object. This request should be made within the timeout window of the [real time authorization](https://stripe.com/docs/issuing/controls/real-time-authorizations) flow.
This method is deprecated. Instead, [respond directly to the webhook request to decline an authorization](https://stripe.com/docs/issuing/controls/real-time-authorizations#authorization-handling).

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `authorization (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |

Returns: `issuing.authorization`

## GET /v1/issuing/cardholders

operationId: `GetIssuingCardholders`

Returns a list of Issuing `Cardholder` objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | object or integer |  | Only return cardholders that were created during the given date interval. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `email` | string |  | Only return cardholders that have the given email address. |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `phone_number` | string |  | Only return cardholders that have the given phone number. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `status` | enum: `active`, `blocked`, `inactive` |  | Only return cardholders that have the given status. One of `active`, `inactive`, or `blocked`. |
| `type` | enum: `company`, `individual` |  | Only return cardholders that have the given type. One of `individual` or `company`. |

Returns: object

## POST /v1/issuing/cardholders

operationId: `PostIssuingCardholders`

Creates a new Issuing `Cardholder` object that can be issued cards.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `billing` | object | yes | The cardholder's billing address. |
| `billing.address` | object | yes |  |
| `billing.address.city` | string | yes |  |
| `billing.address.country` | string | yes |  |
| `billing.address.line1` | string | yes |  |
| `billing.address.line2` | string |  |  |
| `billing.address.postal_code` | string | yes |  |
| `billing.address.state` | string |  |  |
| `company` | object |  | Additional information about a `company` cardholder. |
| `company.tax_id` | string |  |  |
| `email` | string |  | The cardholder's email address. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `individual` | object |  | Additional information about an `individual` cardholder. |
| `individual.card_issuing` | object |  |  |
| `individual.card_issuing.user_terms_acceptance` | object |  |  |
| `individual.card_issuing.user_terms_acceptance.date` | timestamp (Unix seconds) |  |  |
| `individual.card_issuing.user_terms_acceptance.ip` | string |  |  |
| `individual.card_issuing.user_terms_acceptance.user_agent` | string or "" (to unset) |  |  |
| `individual.dob` | object |  |  |
| `individual.dob.day` | integer | yes |  |
| `individual.dob.month` | integer | yes |  |
| `individual.dob.year` | integer | yes |  |
| `individual.first_name` | string |  |  |
| `individual.last_name` | string |  |  |
| `individual.verification` | object |  |  |
| `individual.verification.document` | object |  |  |
| `individual.verification.document.back` | string |  |  |
| `individual.verification.document.front` | string |  |  |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `name` | string | yes | The cardholder's name. This will be printed on cards issued to them. The maximum length of this field is 24 characters. This field cannot contain any special characters or numbers. |
| `phone_number` | string |  | The cardholder's phone number. This will be transformed to [E.164](https://en.wikipedia.org/wiki/E.164) if it is not provided in that format already. This is required for all cardholders who will be creating EU cards. See the [3D Secure documentation](https://stripe.com/docs/issuing/3d-secure#when-is-3d-secure-applied) for more details. |
| `preferred_locales` | array of enum: `de`, `en`, `es`, `fr`, `it` |  | The cardholder’s preferred locales (languages), ordered by preference. Locales can be `de`, `en`, `es`, `fr`, or `it`.  This changes the language of the [3D Secure flow](https://stripe.com/docs/issuing/3d-secure) and one-time password messages sent to the cardholder. |
| `spending_controls` | object |  | Rules that control spending across this cardholder's cards. Refer to our [documentation](https://stripe.com/docs/issuing/controls/spending-controls) for more details. |
| `spending_controls.allowed_categories` | array of enum: `ac_refrigeration_repair`, `accounting_bookkeeping_services`, `advertising_services`, `agricultural_cooperative`, `airlines_air_carriers`, `airports_flying_fields`, `ambulance_services`, `amusement_parks_carnivals`, `antique_reproductions`, `antique_shops`, `aquariums`, `architectural_surveying_services`, `art_dealers_and_galleries`, `artists_supply_and_craft_shops`, `auto_and_home_supply_stores`, `auto_body_repair_shops`, `auto_paint_shops`, `auto_service_shops`, `automated_cash_disburse`, `automated_fuel_dispensers`, `automobile_associations`, `automotive_parts_and_accessories_stores`, `automotive_tire_stores`, `bail_and_bond_payments`, `bakeries`, `bands_orchestras`, `barber_and_beauty_shops`, `betting_casino_gambling`, `bicycle_shops`, `billiard_pool_establishments`, `boat_dealers`, `boat_rentals_and_leases`, `book_stores`, `books_periodicals_and_newspapers`, `bowling_alleys`, `bus_lines`, `business_secretarial_schools`, `buying_shopping_services`, `cable_satellite_and_other_pay_television_and_radio`, `camera_and_photographic_supply_stores`, `candy_nut_and_confectionery_stores`, `car_and_truck_dealers_new_used`, `car_and_truck_dealers_used_only`, `car_rental_agencies`, `car_washes`, `carpentry_services`, `carpet_upholstery_cleaning`, `caterers`, `charitable_and_social_service_organizations_fundraising`, `chemicals_and_allied_products`, `child_care_services`, `childrens_and_infants_wear_stores`, `chiropodists_podiatrists`, `chiropractors`, `cigar_stores_and_stands`, `civic_social_fraternal_associations`, `cleaning_and_maintenance`, `clothing_rental`, `colleges_universities`, `commercial_equipment`, `commercial_footwear`, `commercial_photography_art_and_graphics`, `commuter_transport_and_ferries`, `computer_network_services`, `computer_programming`, `computer_repair`, `computer_software_stores`, `computers_peripherals_and_software`, `concrete_work_services`, `construction_materials`, `consulting_public_relations`, `correspondence_schools`, `cosmetic_stores`, `counseling_services`, `country_clubs`, `courier_services`, `court_costs`, `credit_reporting_agencies`, `cruise_lines`, `dairy_products_stores`, `dance_hall_studios_schools`, `dating_escort_services`, `dentists_orthodontists`, `department_stores`, `detective_agencies`, `digital_goods_applications`, `digital_goods_games`, `digital_goods_large_volume`, `digital_goods_media`, `direct_marketing_catalog_merchant`, `direct_marketing_combination_catalog_and_retail_merchant`, `direct_marketing_inbound_telemarketing`, `direct_marketing_insurance_services`, `direct_marketing_other`, `direct_marketing_outbound_telemarketing`, `direct_marketing_subscription`, `direct_marketing_travel`, `discount_stores`, `doctors`, `door_to_door_sales`, `drapery_window_covering_and_upholstery_stores`, `drinking_places`, `drug_stores_and_pharmacies`, `drugs_drug_proprietaries_and_druggist_sundries`, `dry_cleaners`, `durable_goods`, `duty_free_stores`, `eating_places_restaurants`, `educational_services`, `electric_razor_stores`, `electric_vehicle_charging`, `electrical_parts_and_equipment`, `electrical_services`, `electronics_repair_shops`, `electronics_stores`, `elementary_secondary_schools`, `emergency_services_gcas_visa_use_only`, `employment_temp_agencies`, `equipment_rental`, `exterminating_services`, `family_clothing_stores`, `fast_food_restaurants`, `financial_institutions`, `fines_government_administrative_entities`, `fireplace_fireplace_screens_and_accessories_stores`, `floor_covering_stores`, `florists`, `florists_supplies_nursery_stock_and_flowers`, `freezer_and_locker_meat_provisioners`, `fuel_dealers_non_automotive`, `funeral_services_crematories`, `furniture_home_furnishings_and_equipment_stores_except_appliances`, `furniture_repair_refinishing`, `furriers_and_fur_shops`, `general_services`, `gift_card_novelty_and_souvenir_shops`, `glass_paint_and_wallpaper_stores`, `glassware_crystal_stores`, `golf_courses_public`, `government_licensed_horse_dog_racing_us_region_only`, `government_licensed_online_casions_online_gambling_us_region_only`, `government_owned_lotteries_non_us_region`, `government_owned_lotteries_us_region_only`, `government_services`, `grocery_stores_supermarkets`, `hardware_equipment_and_supplies`, `hardware_stores`, `health_and_beauty_spas`, `hearing_aids_sales_and_supplies`, `heating_plumbing_a_c`, `hobby_toy_and_game_shops`, `home_supply_warehouse_stores`, `hospitals`, `hotels_motels_and_resorts`, `household_appliance_stores`, `industrial_supplies`, `information_retrieval_services`, `insurance_default`, `insurance_underwriting_premiums`, `intra_company_purchases`, `jewelry_stores_watches_clocks_and_silverware_stores`, `landscaping_services`, `laundries`, `laundry_cleaning_services`, `legal_services_attorneys`, `luggage_and_leather_goods_stores`, `lumber_building_materials_stores`, `manual_cash_disburse`, `marinas_service_and_supplies`, `marketplaces`, `masonry_stonework_and_plaster`, `massage_parlors`, `medical_and_dental_labs`, `medical_dental_ophthalmic_and_hospital_equipment_and_supplies`, `medical_services`, `membership_organizations`, `mens_and_boys_clothing_and_accessories_stores`, `mens_womens_clothing_stores`, `metal_service_centers`, `miscellaneous`, `miscellaneous_apparel_and_accessory_shops`, `miscellaneous_auto_dealers`, `miscellaneous_business_services`, `miscellaneous_food_stores`, `miscellaneous_general_merchandise`, `miscellaneous_general_services`, `miscellaneous_home_furnishing_specialty_stores`, `miscellaneous_publishing_and_printing`, `miscellaneous_recreation_services`, `miscellaneous_repair_shops`, `miscellaneous_specialty_retail`, `mobile_home_dealers`, `motion_picture_theaters`, `motor_freight_carriers_and_trucking`, `motor_homes_dealers`, `motor_vehicle_supplies_and_new_parts`, `motorcycle_shops_and_dealers`, `motorcycle_shops_dealers`, `music_stores_musical_instruments_pianos_and_sheet_music`, `news_dealers_and_newsstands`, `non_fi_money_orders`, `non_fi_stored_value_card_purchase_load`, `nondurable_goods`, `nurseries_lawn_and_garden_supply_stores`, `nursing_personal_care`, `office_and_commercial_furniture`, `opticians_eyeglasses`, `optometrists_ophthalmologist`, `orthopedic_goods_prosthetic_devices`, `osteopaths`, `package_stores_beer_wine_and_liquor`, `paints_varnishes_and_supplies`, `parking_lots_garages`, `passenger_railways`, `pawn_shops`, `pet_shops_pet_food_and_supplies`, `petroleum_and_petroleum_products`, `photo_developing`, `photographic_photocopy_microfilm_equipment_and_supplies`, `photographic_studios`, `picture_video_production`, `piece_goods_notions_and_other_dry_goods`, `plumbing_heating_equipment_and_supplies`, `political_organizations`, `postal_services_government_only`, `precious_stones_and_metals_watches_and_jewelry`, `professional_services`, `public_warehousing_and_storage`, `quick_copy_repro_and_blueprint`, `railroads`, `real_estate_agents_and_managers_rentals`, `record_stores`, `recreational_vehicle_rentals`, `religious_goods_stores`, `religious_organizations`, `roofing_siding_sheet_metal`, `secretarial_support_services`, `security_brokers_dealers`, `service_stations`, `sewing_needlework_fabric_and_piece_goods_stores`, `shoe_repair_hat_cleaning`, `shoe_stores`, `small_appliance_repair`, `snowmobile_dealers`, `special_trade_services`, `specialty_cleaning`, `sporting_goods_stores`, `sporting_recreation_camps`, `sports_and_riding_apparel_stores`, `sports_clubs_fields`, `stamp_and_coin_stores`, `stationary_office_supplies_printing_and_writing_paper`, `stationery_stores_office_and_school_supply_stores`, `swimming_pools_sales`, `t_ui_travel_germany`, `tailors_alterations`, `tax_payments_government_agencies`, `tax_preparation_services`, `taxicabs_limousines`, `telecommunication_equipment_and_telephone_sales`, `telecommunication_services`, `telegraph_services`, `tent_and_awning_shops`, `testing_laboratories`, `theatrical_ticket_agencies`, `timeshares`, `tire_retreading_and_repair`, `tolls_bridge_fees`, `tourist_attractions_and_exhibits`, `towing_services`, `trailer_parks_campgrounds`, `transportation_services`, `travel_agencies_tour_operators`, `truck_stop_iteration`, `truck_utility_trailer_rentals`, `typesetting_plate_making_and_related_services`, `typewriter_stores`, `u_s_federal_government_agencies_or_departments`, `uniforms_commercial_clothing`, `used_merchandise_and_secondhand_stores`, `utilities`, `variety_stores`, `veterinary_services`, `video_amusement_game_supplies`, `video_game_arcades`, `video_tape_rental_stores`, `vocational_trade_schools`, `watch_jewelry_repair`, `welding_repair`, `wholesale_clubs`, `wig_and_toupee_stores`, `wires_money_orders`, `womens_accessory_and_specialty_shops`, `womens_ready_to_wear_stores`, `wrecking_and_salvage_yards` |  |  |
| `spending_controls.allowed_merchant_countries` | array of string |  |  |
| `spending_controls.blocked_categories` | array of enum: `ac_refrigeration_repair`, `accounting_bookkeeping_services`, `advertising_services`, `agricultural_cooperative`, `airlines_air_carriers`, `airports_flying_fields`, `ambulance_services`, `amusement_parks_carnivals`, `antique_reproductions`, `antique_shops`, `aquariums`, `architectural_surveying_services`, `art_dealers_and_galleries`, `artists_supply_and_craft_shops`, `auto_and_home_supply_stores`, `auto_body_repair_shops`, `auto_paint_shops`, `auto_service_shops`, `automated_cash_disburse`, `automated_fuel_dispensers`, `automobile_associations`, `automotive_parts_and_accessories_stores`, `automotive_tire_stores`, `bail_and_bond_payments`, `bakeries`, `bands_orchestras`, `barber_and_beauty_shops`, `betting_casino_gambling`, `bicycle_shops`, `billiard_pool_establishments`, `boat_dealers`, `boat_rentals_and_leases`, `book_stores`, `books_periodicals_and_newspapers`, `bowling_alleys`, `bus_lines`, `business_secretarial_schools`, `buying_shopping_services`, `cable_satellite_and_other_pay_television_and_radio`, `camera_and_photographic_supply_stores`, `candy_nut_and_confectionery_stores`, `car_and_truck_dealers_new_used`, `car_and_truck_dealers_used_only`, `car_rental_agencies`, `car_washes`, `carpentry_services`, `carpet_upholstery_cleaning`, `caterers`, `charitable_and_social_service_organizations_fundraising`, `chemicals_and_allied_products`, `child_care_services`, `childrens_and_infants_wear_stores`, `chiropodists_podiatrists`, `chiropractors`, `cigar_stores_and_stands`, `civic_social_fraternal_associations`, `cleaning_and_maintenance`, `clothing_rental`, `colleges_universities`, `commercial_equipment`, `commercial_footwear`, `commercial_photography_art_and_graphics`, `commuter_transport_and_ferries`, `computer_network_services`, `computer_programming`, `computer_repair`, `computer_software_stores`, `computers_peripherals_and_software`, `concrete_work_services`, `construction_materials`, `consulting_public_relations`, `correspondence_schools`, `cosmetic_stores`, `counseling_services`, `country_clubs`, `courier_services`, `court_costs`, `credit_reporting_agencies`, `cruise_lines`, `dairy_products_stores`, `dance_hall_studios_schools`, `dating_escort_services`, `dentists_orthodontists`, `department_stores`, `detective_agencies`, `digital_goods_applications`, `digital_goods_games`, `digital_goods_large_volume`, `digital_goods_media`, `direct_marketing_catalog_merchant`, `direct_marketing_combination_catalog_and_retail_merchant`, `direct_marketing_inbound_telemarketing`, `direct_marketing_insurance_services`, `direct_marketing_other`, `direct_marketing_outbound_telemarketing`, `direct_marketing_subscription`, `direct_marketing_travel`, `discount_stores`, `doctors`, `door_to_door_sales`, `drapery_window_covering_and_upholstery_stores`, `drinking_places`, `drug_stores_and_pharmacies`, `drugs_drug_proprietaries_and_druggist_sundries`, `dry_cleaners`, `durable_goods`, `duty_free_stores`, `eating_places_restaurants`, `educational_services`, `electric_razor_stores`, `electric_vehicle_charging`, `electrical_parts_and_equipment`, `electrical_services`, `electronics_repair_shops`, `electronics_stores`, `elementary_secondary_schools`, `emergency_services_gcas_visa_use_only`, `employment_temp_agencies`, `equipment_rental`, `exterminating_services`, `family_clothing_stores`, `fast_food_restaurants`, `financial_institutions`, `fines_government_administrative_entities`, `fireplace_fireplace_screens_and_accessories_stores`, `floor_covering_stores`, `florists`, `florists_supplies_nursery_stock_and_flowers`, `freezer_and_locker_meat_provisioners`, `fuel_dealers_non_automotive`, `funeral_services_crematories`, `furniture_home_furnishings_and_equipment_stores_except_appliances`, `furniture_repair_refinishing`, `furriers_and_fur_shops`, `general_services`, `gift_card_novelty_and_souvenir_shops`, `glass_paint_and_wallpaper_stores`, `glassware_crystal_stores`, `golf_courses_public`, `government_licensed_horse_dog_racing_us_region_only`, `government_licensed_online_casions_online_gambling_us_region_only`, `government_owned_lotteries_non_us_region`, `government_owned_lotteries_us_region_only`, `government_services`, `grocery_stores_supermarkets`, `hardware_equipment_and_supplies`, `hardware_stores`, `health_and_beauty_spas`, `hearing_aids_sales_and_supplies`, `heating_plumbing_a_c`, `hobby_toy_and_game_shops`, `home_supply_warehouse_stores`, `hospitals`, `hotels_motels_and_resorts`, `household_appliance_stores`, `industrial_supplies`, `information_retrieval_services`, `insurance_default`, `insurance_underwriting_premiums`, `intra_company_purchases`, `jewelry_stores_watches_clocks_and_silverware_stores`, `landscaping_services`, `laundries`, `laundry_cleaning_services`, `legal_services_attorneys`, `luggage_and_leather_goods_stores`, `lumber_building_materials_stores`, `manual_cash_disburse`, `marinas_service_and_supplies`, `marketplaces`, `masonry_stonework_and_plaster`, `massage_parlors`, `medical_and_dental_labs`, `medical_dental_ophthalmic_and_hospital_equipment_and_supplies`, `medical_services`, `membership_organizations`, `mens_and_boys_clothing_and_accessories_stores`, `mens_womens_clothing_stores`, `metal_service_centers`, `miscellaneous`, `miscellaneous_apparel_and_accessory_shops`, `miscellaneous_auto_dealers`, `miscellaneous_business_services`, `miscellaneous_food_stores`, `miscellaneous_general_merchandise`, `miscellaneous_general_services`, `miscellaneous_home_furnishing_specialty_stores`, `miscellaneous_publishing_and_printing`, `miscellaneous_recreation_services`, `miscellaneous_repair_shops`, `miscellaneous_specialty_retail`, `mobile_home_dealers`, `motion_picture_theaters`, `motor_freight_carriers_and_trucking`, `motor_homes_dealers`, `motor_vehicle_supplies_and_new_parts`, `motorcycle_shops_and_dealers`, `motorcycle_shops_dealers`, `music_stores_musical_instruments_pianos_and_sheet_music`, `news_dealers_and_newsstands`, `non_fi_money_orders`, `non_fi_stored_value_card_purchase_load`, `nondurable_goods`, `nurseries_lawn_and_garden_supply_stores`, `nursing_personal_care`, `office_and_commercial_furniture`, `opticians_eyeglasses`, `optometrists_ophthalmologist`, `orthopedic_goods_prosthetic_devices`, `osteopaths`, `package_stores_beer_wine_and_liquor`, `paints_varnishes_and_supplies`, `parking_lots_garages`, `passenger_railways`, `pawn_shops`, `pet_shops_pet_food_and_supplies`, `petroleum_and_petroleum_products`, `photo_developing`, `photographic_photocopy_microfilm_equipment_and_supplies`, `photographic_studios`, `picture_video_production`, `piece_goods_notions_and_other_dry_goods`, `plumbing_heating_equipment_and_supplies`, `political_organizations`, `postal_services_government_only`, `precious_stones_and_metals_watches_and_jewelry`, `professional_services`, `public_warehousing_and_storage`, `quick_copy_repro_and_blueprint`, `railroads`, `real_estate_agents_and_managers_rentals`, `record_stores`, `recreational_vehicle_rentals`, `religious_goods_stores`, `religious_organizations`, `roofing_siding_sheet_metal`, `secretarial_support_services`, `security_brokers_dealers`, `service_stations`, `sewing_needlework_fabric_and_piece_goods_stores`, `shoe_repair_hat_cleaning`, `shoe_stores`, `small_appliance_repair`, `snowmobile_dealers`, `special_trade_services`, `specialty_cleaning`, `sporting_goods_stores`, `sporting_recreation_camps`, `sports_and_riding_apparel_stores`, `sports_clubs_fields`, `stamp_and_coin_stores`, `stationary_office_supplies_printing_and_writing_paper`, `stationery_stores_office_and_school_supply_stores`, `swimming_pools_sales`, `t_ui_travel_germany`, `tailors_alterations`, `tax_payments_government_agencies`, `tax_preparation_services`, `taxicabs_limousines`, `telecommunication_equipment_and_telephone_sales`, `telecommunication_services`, `telegraph_services`, `tent_and_awning_shops`, `testing_laboratories`, `theatrical_ticket_agencies`, `timeshares`, `tire_retreading_and_repair`, `tolls_bridge_fees`, `tourist_attractions_and_exhibits`, `towing_services`, `trailer_parks_campgrounds`, `transportation_services`, `travel_agencies_tour_operators`, `truck_stop_iteration`, `truck_utility_trailer_rentals`, `typesetting_plate_making_and_related_services`, `typewriter_stores`, `u_s_federal_government_agencies_or_departments`, `uniforms_commercial_clothing`, `used_merchandise_and_secondhand_stores`, `utilities`, `variety_stores`, `veterinary_services`, `video_amusement_game_supplies`, `video_game_arcades`, `video_tape_rental_stores`, `vocational_trade_schools`, `watch_jewelry_repair`, `welding_repair`, `wholesale_clubs`, `wig_and_toupee_stores`, `wires_money_orders`, `womens_accessory_and_specialty_shops`, `womens_ready_to_wear_stores`, `wrecking_and_salvage_yards` |  |  |
| `spending_controls.blocked_merchant_countries` | array of string |  |  |
| `spending_controls.spending_limits` | array of object |  |  |
| `spending_controls.spending_limits[].amount` | integer | yes |  |
| `spending_controls.spending_limits[].categories` | array of enum: `ac_refrigeration_repair`, `accounting_bookkeeping_services`, `advertising_services`, `agricultural_cooperative`, `airlines_air_carriers`, `airports_flying_fields`, `ambulance_services`, `amusement_parks_carnivals`, `antique_reproductions`, `antique_shops`, `aquariums`, `architectural_surveying_services`, `art_dealers_and_galleries`, `artists_supply_and_craft_shops`, `auto_and_home_supply_stores`, `auto_body_repair_shops`, `auto_paint_shops`, `auto_service_shops`, `automated_cash_disburse`, `automated_fuel_dispensers`, `automobile_associations`, `automotive_parts_and_accessories_stores`, `automotive_tire_stores`, `bail_and_bond_payments`, `bakeries`, `bands_orchestras`, `barber_and_beauty_shops`, `betting_casino_gambling`, `bicycle_shops`, `billiard_pool_establishments`, `boat_dealers`, `boat_rentals_and_leases`, `book_stores`, `books_periodicals_and_newspapers`, `bowling_alleys`, `bus_lines`, `business_secretarial_schools`, `buying_shopping_services`, `cable_satellite_and_other_pay_television_and_radio`, `camera_and_photographic_supply_stores`, `candy_nut_and_confectionery_stores`, `car_and_truck_dealers_new_used`, `car_and_truck_dealers_used_only`, `car_rental_agencies`, `car_washes`, `carpentry_services`, `carpet_upholstery_cleaning`, `caterers`, `charitable_and_social_service_organizations_fundraising`, `chemicals_and_allied_products`, `child_care_services`, `childrens_and_infants_wear_stores`, `chiropodists_podiatrists`, `chiropractors`, `cigar_stores_and_stands`, `civic_social_fraternal_associations`, `cleaning_and_maintenance`, `clothing_rental`, `colleges_universities`, `commercial_equipment`, `commercial_footwear`, `commercial_photography_art_and_graphics`, `commuter_transport_and_ferries`, `computer_network_services`, `computer_programming`, `computer_repair`, `computer_software_stores`, `computers_peripherals_and_software`, `concrete_work_services`, `construction_materials`, `consulting_public_relations`, `correspondence_schools`, `cosmetic_stores`, `counseling_services`, `country_clubs`, `courier_services`, `court_costs`, `credit_reporting_agencies`, `cruise_lines`, `dairy_products_stores`, `dance_hall_studios_schools`, `dating_escort_services`, `dentists_orthodontists`, `department_stores`, `detective_agencies`, `digital_goods_applications`, `digital_goods_games`, `digital_goods_large_volume`, `digital_goods_media`, `direct_marketing_catalog_merchant`, `direct_marketing_combination_catalog_and_retail_merchant`, `direct_marketing_inbound_telemarketing`, `direct_marketing_insurance_services`, `direct_marketing_other`, `direct_marketing_outbound_telemarketing`, `direct_marketing_subscription`, `direct_marketing_travel`, `discount_stores`, `doctors`, `door_to_door_sales`, `drapery_window_covering_and_upholstery_stores`, `drinking_places`, `drug_stores_and_pharmacies`, `drugs_drug_proprietaries_and_druggist_sundries`, `dry_cleaners`, `durable_goods`, `duty_free_stores`, `eating_places_restaurants`, `educational_services`, `electric_razor_stores`, `electric_vehicle_charging`, `electrical_parts_and_equipment`, `electrical_services`, `electronics_repair_shops`, `electronics_stores`, `elementary_secondary_schools`, `emergency_services_gcas_visa_use_only`, `employment_temp_agencies`, `equipment_rental`, `exterminating_services`, `family_clothing_stores`, `fast_food_restaurants`, `financial_institutions`, `fines_government_administrative_entities`, `fireplace_fireplace_screens_and_accessories_stores`, `floor_covering_stores`, `florists`, `florists_supplies_nursery_stock_and_flowers`, `freezer_and_locker_meat_provisioners`, `fuel_dealers_non_automotive`, `funeral_services_crematories`, `furniture_home_furnishings_and_equipment_stores_except_appliances`, `furniture_repair_refinishing`, `furriers_and_fur_shops`, `general_services`, `gift_card_novelty_and_souvenir_shops`, `glass_paint_and_wallpaper_stores`, `glassware_crystal_stores`, `golf_courses_public`, `government_licensed_horse_dog_racing_us_region_only`, `government_licensed_online_casions_online_gambling_us_region_only`, `government_owned_lotteries_non_us_region`, `government_owned_lotteries_us_region_only`, `government_services`, `grocery_stores_supermarkets`, `hardware_equipment_and_supplies`, `hardware_stores`, `health_and_beauty_spas`, `hearing_aids_sales_and_supplies`, `heating_plumbing_a_c`, `hobby_toy_and_game_shops`, `home_supply_warehouse_stores`, `hospitals`, `hotels_motels_and_resorts`, `household_appliance_stores`, `industrial_supplies`, `information_retrieval_services`, `insurance_default`, `insurance_underwriting_premiums`, `intra_company_purchases`, `jewelry_stores_watches_clocks_and_silverware_stores`, `landscaping_services`, `laundries`, `laundry_cleaning_services`, `legal_services_attorneys`, `luggage_and_leather_goods_stores`, `lumber_building_materials_stores`, `manual_cash_disburse`, `marinas_service_and_supplies`, `marketplaces`, `masonry_stonework_and_plaster`, `massage_parlors`, `medical_and_dental_labs`, `medical_dental_ophthalmic_and_hospital_equipment_and_supplies`, `medical_services`, `membership_organizations`, `mens_and_boys_clothing_and_accessories_stores`, `mens_womens_clothing_stores`, `metal_service_centers`, `miscellaneous`, `miscellaneous_apparel_and_accessory_shops`, `miscellaneous_auto_dealers`, `miscellaneous_business_services`, `miscellaneous_food_stores`, `miscellaneous_general_merchandise`, `miscellaneous_general_services`, `miscellaneous_home_furnishing_specialty_stores`, `miscellaneous_publishing_and_printing`, `miscellaneous_recreation_services`, `miscellaneous_repair_shops`, `miscellaneous_specialty_retail`, `mobile_home_dealers`, `motion_picture_theaters`, `motor_freight_carriers_and_trucking`, `motor_homes_dealers`, `motor_vehicle_supplies_and_new_parts`, `motorcycle_shops_and_dealers`, `motorcycle_shops_dealers`, `music_stores_musical_instruments_pianos_and_sheet_music`, `news_dealers_and_newsstands`, `non_fi_money_orders`, `non_fi_stored_value_card_purchase_load`, `nondurable_goods`, `nurseries_lawn_and_garden_supply_stores`, `nursing_personal_care`, `office_and_commercial_furniture`, `opticians_eyeglasses`, `optometrists_ophthalmologist`, `orthopedic_goods_prosthetic_devices`, `osteopaths`, `package_stores_beer_wine_and_liquor`, `paints_varnishes_and_supplies`, `parking_lots_garages`, `passenger_railways`, `pawn_shops`, `pet_shops_pet_food_and_supplies`, `petroleum_and_petroleum_products`, `photo_developing`, `photographic_photocopy_microfilm_equipment_and_supplies`, `photographic_studios`, `picture_video_production`, `piece_goods_notions_and_other_dry_goods`, `plumbing_heating_equipment_and_supplies`, `political_organizations`, `postal_services_government_only`, `precious_stones_and_metals_watches_and_jewelry`, `professional_services`, `public_warehousing_and_storage`, `quick_copy_repro_and_blueprint`, `railroads`, `real_estate_agents_and_managers_rentals`, `record_stores`, `recreational_vehicle_rentals`, `religious_goods_stores`, `religious_organizations`, `roofing_siding_sheet_metal`, `secretarial_support_services`, `security_brokers_dealers`, `service_stations`, `sewing_needlework_fabric_and_piece_goods_stores`, `shoe_repair_hat_cleaning`, `shoe_stores`, `small_appliance_repair`, `snowmobile_dealers`, `special_trade_services`, `specialty_cleaning`, `sporting_goods_stores`, `sporting_recreation_camps`, `sports_and_riding_apparel_stores`, `sports_clubs_fields`, `stamp_and_coin_stores`, `stationary_office_supplies_printing_and_writing_paper`, `stationery_stores_office_and_school_supply_stores`, `swimming_pools_sales`, `t_ui_travel_germany`, `tailors_alterations`, `tax_payments_government_agencies`, `tax_preparation_services`, `taxicabs_limousines`, `telecommunication_equipment_and_telephone_sales`, `telecommunication_services`, `telegraph_services`, `tent_and_awning_shops`, `testing_laboratories`, `theatrical_ticket_agencies`, `timeshares`, `tire_retreading_and_repair`, `tolls_bridge_fees`, `tourist_attractions_and_exhibits`, `towing_services`, `trailer_parks_campgrounds`, `transportation_services`, `travel_agencies_tour_operators`, `truck_stop_iteration`, `truck_utility_trailer_rentals`, `typesetting_plate_making_and_related_services`, `typewriter_stores`, `u_s_federal_government_agencies_or_departments`, `uniforms_commercial_clothing`, `used_merchandise_and_secondhand_stores`, `utilities`, `variety_stores`, `veterinary_services`, `video_amusement_game_supplies`, `video_game_arcades`, `video_tape_rental_stores`, `vocational_trade_schools`, `watch_jewelry_repair`, `welding_repair`, `wholesale_clubs`, `wig_and_toupee_stores`, `wires_money_orders`, `womens_accessory_and_specialty_shops`, `womens_ready_to_wear_stores`, `wrecking_and_salvage_yards` |  |  |
| `spending_controls.spending_limits[].interval` | enum: `all_time`, `daily`, `monthly`, `per_authorization`, `weekly`, `yearly` | yes |  |
| `spending_controls.spending_limits_currency` | string |  |  |
| `status` | enum: `active`, `inactive` |  | Specifies whether to permit authorizations on this cardholder's cards. Defaults to `active`. |
| `type` | enum: `company`, `individual` |  | One of `individual` or `company`. See [Choose a cardholder type](https://stripe.com/docs/issuing/other/choose-cardholder) for more details. |

Returns: `issuing.cardholder`

## GET /v1/issuing/cardholders/{cardholder}

operationId: `GetIssuingCardholdersCardholder`

Retrieves an Issuing `Cardholder` object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `cardholder (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `issuing.cardholder`

## POST /v1/issuing/cardholders/{cardholder}

operationId: `PostIssuingCardholdersCardholder`

Updates the specified Issuing `Cardholder` object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `cardholder (path)` | string | yes |  |
| `billing` | object |  | The cardholder's billing address. |
| `billing.address` | object | yes |  |
| `billing.address.city` | string | yes |  |
| `billing.address.country` | string | yes |  |
| `billing.address.line1` | string | yes |  |
| `billing.address.line2` | string |  |  |
| `billing.address.postal_code` | string | yes |  |
| `billing.address.state` | string |  |  |
| `company` | object |  | Additional information about a `company` cardholder. |
| `company.tax_id` | string |  |  |
| `email` | string |  | The cardholder's email address. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `individual` | object |  | Additional information about an `individual` cardholder. |
| `individual.card_issuing` | object |  |  |
| `individual.card_issuing.user_terms_acceptance` | object |  |  |
| `individual.card_issuing.user_terms_acceptance.date` | timestamp (Unix seconds) |  |  |
| `individual.card_issuing.user_terms_acceptance.ip` | string |  |  |
| `individual.card_issuing.user_terms_acceptance.user_agent` | string or "" (to unset) |  |  |
| `individual.dob` | object |  |  |
| `individual.dob.day` | integer | yes |  |
| `individual.dob.month` | integer | yes |  |
| `individual.dob.year` | integer | yes |  |
| `individual.first_name` | string |  |  |
| `individual.last_name` | string |  |  |
| `individual.verification` | object |  |  |
| `individual.verification.document` | object |  |  |
| `individual.verification.document.back` | string |  |  |
| `individual.verification.document.front` | string |  |  |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `phone_number` | string |  | The cardholder's phone number. This is required for all cardholders who will be creating EU cards. See the [3D Secure documentation](https://stripe.com/docs/issuing/3d-secure) for more details. |
| `preferred_locales` | array of enum: `de`, `en`, `es`, `fr`, `it` |  | The cardholder’s preferred locales (languages), ordered by preference. Locales can be `de`, `en`, `es`, `fr`, or `it`.  This changes the language of the [3D Secure flow](https://stripe.com/docs/issuing/3d-secure) and one-time password messages sent to the cardholder. |
| `spending_controls` | object |  | Rules that control spending across this cardholder's cards. Refer to our [documentation](https://stripe.com/docs/issuing/controls/spending-controls) for more details. |
| `spending_controls.allowed_categories` | array of enum: `ac_refrigeration_repair`, `accounting_bookkeeping_services`, `advertising_services`, `agricultural_cooperative`, `airlines_air_carriers`, `airports_flying_fields`, `ambulance_services`, `amusement_parks_carnivals`, `antique_reproductions`, `antique_shops`, `aquariums`, `architectural_surveying_services`, `art_dealers_and_galleries`, `artists_supply_and_craft_shops`, `auto_and_home_supply_stores`, `auto_body_repair_shops`, `auto_paint_shops`, `auto_service_shops`, `automated_cash_disburse`, `automated_fuel_dispensers`, `automobile_associations`, `automotive_parts_and_accessories_stores`, `automotive_tire_stores`, `bail_and_bond_payments`, `bakeries`, `bands_orchestras`, `barber_and_beauty_shops`, `betting_casino_gambling`, `bicycle_shops`, `billiard_pool_establishments`, `boat_dealers`, `boat_rentals_and_leases`, `book_stores`, `books_periodicals_and_newspapers`, `bowling_alleys`, `bus_lines`, `business_secretarial_schools`, `buying_shopping_services`, `cable_satellite_and_other_pay_television_and_radio`, `camera_and_photographic_supply_stores`, `candy_nut_and_confectionery_stores`, `car_and_truck_dealers_new_used`, `car_and_truck_dealers_used_only`, `car_rental_agencies`, `car_washes`, `carpentry_services`, `carpet_upholstery_cleaning`, `caterers`, `charitable_and_social_service_organizations_fundraising`, `chemicals_and_allied_products`, `child_care_services`, `childrens_and_infants_wear_stores`, `chiropodists_podiatrists`, `chiropractors`, `cigar_stores_and_stands`, `civic_social_fraternal_associations`, `cleaning_and_maintenance`, `clothing_rental`, `colleges_universities`, `commercial_equipment`, `commercial_footwear`, `commercial_photography_art_and_graphics`, `commuter_transport_and_ferries`, `computer_network_services`, `computer_programming`, `computer_repair`, `computer_software_stores`, `computers_peripherals_and_software`, `concrete_work_services`, `construction_materials`, `consulting_public_relations`, `correspondence_schools`, `cosmetic_stores`, `counseling_services`, `country_clubs`, `courier_services`, `court_costs`, `credit_reporting_agencies`, `cruise_lines`, `dairy_products_stores`, `dance_hall_studios_schools`, `dating_escort_services`, `dentists_orthodontists`, `department_stores`, `detective_agencies`, `digital_goods_applications`, `digital_goods_games`, `digital_goods_large_volume`, `digital_goods_media`, `direct_marketing_catalog_merchant`, `direct_marketing_combination_catalog_and_retail_merchant`, `direct_marketing_inbound_telemarketing`, `direct_marketing_insurance_services`, `direct_marketing_other`, `direct_marketing_outbound_telemarketing`, `direct_marketing_subscription`, `direct_marketing_travel`, `discount_stores`, `doctors`, `door_to_door_sales`, `drapery_window_covering_and_upholstery_stores`, `drinking_places`, `drug_stores_and_pharmacies`, `drugs_drug_proprietaries_and_druggist_sundries`, `dry_cleaners`, `durable_goods`, `duty_free_stores`, `eating_places_restaurants`, `educational_services`, `electric_razor_stores`, `electric_vehicle_charging`, `electrical_parts_and_equipment`, `electrical_services`, `electronics_repair_shops`, `electronics_stores`, `elementary_secondary_schools`, `emergency_services_gcas_visa_use_only`, `employment_temp_agencies`, `equipment_rental`, `exterminating_services`, `family_clothing_stores`, `fast_food_restaurants`, `financial_institutions`, `fines_government_administrative_entities`, `fireplace_fireplace_screens_and_accessories_stores`, `floor_covering_stores`, `florists`, `florists_supplies_nursery_stock_and_flowers`, `freezer_and_locker_meat_provisioners`, `fuel_dealers_non_automotive`, `funeral_services_crematories`, `furniture_home_furnishings_and_equipment_stores_except_appliances`, `furniture_repair_refinishing`, `furriers_and_fur_shops`, `general_services`, `gift_card_novelty_and_souvenir_shops`, `glass_paint_and_wallpaper_stores`, `glassware_crystal_stores`, `golf_courses_public`, `government_licensed_horse_dog_racing_us_region_only`, `government_licensed_online_casions_online_gambling_us_region_only`, `government_owned_lotteries_non_us_region`, `government_owned_lotteries_us_region_only`, `government_services`, `grocery_stores_supermarkets`, `hardware_equipment_and_supplies`, `hardware_stores`, `health_and_beauty_spas`, `hearing_aids_sales_and_supplies`, `heating_plumbing_a_c`, `hobby_toy_and_game_shops`, `home_supply_warehouse_stores`, `hospitals`, `hotels_motels_and_resorts`, `household_appliance_stores`, `industrial_supplies`, `information_retrieval_services`, `insurance_default`, `insurance_underwriting_premiums`, `intra_company_purchases`, `jewelry_stores_watches_clocks_and_silverware_stores`, `landscaping_services`, `laundries`, `laundry_cleaning_services`, `legal_services_attorneys`, `luggage_and_leather_goods_stores`, `lumber_building_materials_stores`, `manual_cash_disburse`, `marinas_service_and_supplies`, `marketplaces`, `masonry_stonework_and_plaster`, `massage_parlors`, `medical_and_dental_labs`, `medical_dental_ophthalmic_and_hospital_equipment_and_supplies`, `medical_services`, `membership_organizations`, `mens_and_boys_clothing_and_accessories_stores`, `mens_womens_clothing_stores`, `metal_service_centers`, `miscellaneous`, `miscellaneous_apparel_and_accessory_shops`, `miscellaneous_auto_dealers`, `miscellaneous_business_services`, `miscellaneous_food_stores`, `miscellaneous_general_merchandise`, `miscellaneous_general_services`, `miscellaneous_home_furnishing_specialty_stores`, `miscellaneous_publishing_and_printing`, `miscellaneous_recreation_services`, `miscellaneous_repair_shops`, `miscellaneous_specialty_retail`, `mobile_home_dealers`, `motion_picture_theaters`, `motor_freight_carriers_and_trucking`, `motor_homes_dealers`, `motor_vehicle_supplies_and_new_parts`, `motorcycle_shops_and_dealers`, `motorcycle_shops_dealers`, `music_stores_musical_instruments_pianos_and_sheet_music`, `news_dealers_and_newsstands`, `non_fi_money_orders`, `non_fi_stored_value_card_purchase_load`, `nondurable_goods`, `nurseries_lawn_and_garden_supply_stores`, `nursing_personal_care`, `office_and_commercial_furniture`, `opticians_eyeglasses`, `optometrists_ophthalmologist`, `orthopedic_goods_prosthetic_devices`, `osteopaths`, `package_stores_beer_wine_and_liquor`, `paints_varnishes_and_supplies`, `parking_lots_garages`, `passenger_railways`, `pawn_shops`, `pet_shops_pet_food_and_supplies`, `petroleum_and_petroleum_products`, `photo_developing`, `photographic_photocopy_microfilm_equipment_and_supplies`, `photographic_studios`, `picture_video_production`, `piece_goods_notions_and_other_dry_goods`, `plumbing_heating_equipment_and_supplies`, `political_organizations`, `postal_services_government_only`, `precious_stones_and_metals_watches_and_jewelry`, `professional_services`, `public_warehousing_and_storage`, `quick_copy_repro_and_blueprint`, `railroads`, `real_estate_agents_and_managers_rentals`, `record_stores`, `recreational_vehicle_rentals`, `religious_goods_stores`, `religious_organizations`, `roofing_siding_sheet_metal`, `secretarial_support_services`, `security_brokers_dealers`, `service_stations`, `sewing_needlework_fabric_and_piece_goods_stores`, `shoe_repair_hat_cleaning`, `shoe_stores`, `small_appliance_repair`, `snowmobile_dealers`, `special_trade_services`, `specialty_cleaning`, `sporting_goods_stores`, `sporting_recreation_camps`, `sports_and_riding_apparel_stores`, `sports_clubs_fields`, `stamp_and_coin_stores`, `stationary_office_supplies_printing_and_writing_paper`, `stationery_stores_office_and_school_supply_stores`, `swimming_pools_sales`, `t_ui_travel_germany`, `tailors_alterations`, `tax_payments_government_agencies`, `tax_preparation_services`, `taxicabs_limousines`, `telecommunication_equipment_and_telephone_sales`, `telecommunication_services`, `telegraph_services`, `tent_and_awning_shops`, `testing_laboratories`, `theatrical_ticket_agencies`, `timeshares`, `tire_retreading_and_repair`, `tolls_bridge_fees`, `tourist_attractions_and_exhibits`, `towing_services`, `trailer_parks_campgrounds`, `transportation_services`, `travel_agencies_tour_operators`, `truck_stop_iteration`, `truck_utility_trailer_rentals`, `typesetting_plate_making_and_related_services`, `typewriter_stores`, `u_s_federal_government_agencies_or_departments`, `uniforms_commercial_clothing`, `used_merchandise_and_secondhand_stores`, `utilities`, `variety_stores`, `veterinary_services`, `video_amusement_game_supplies`, `video_game_arcades`, `video_tape_rental_stores`, `vocational_trade_schools`, `watch_jewelry_repair`, `welding_repair`, `wholesale_clubs`, `wig_and_toupee_stores`, `wires_money_orders`, `womens_accessory_and_specialty_shops`, `womens_ready_to_wear_stores`, `wrecking_and_salvage_yards` |  |  |
| `spending_controls.allowed_merchant_countries` | array of string |  |  |
| `spending_controls.blocked_categories` | array of enum: `ac_refrigeration_repair`, `accounting_bookkeeping_services`, `advertising_services`, `agricultural_cooperative`, `airlines_air_carriers`, `airports_flying_fields`, `ambulance_services`, `amusement_parks_carnivals`, `antique_reproductions`, `antique_shops`, `aquariums`, `architectural_surveying_services`, `art_dealers_and_galleries`, `artists_supply_and_craft_shops`, `auto_and_home_supply_stores`, `auto_body_repair_shops`, `auto_paint_shops`, `auto_service_shops`, `automated_cash_disburse`, `automated_fuel_dispensers`, `automobile_associations`, `automotive_parts_and_accessories_stores`, `automotive_tire_stores`, `bail_and_bond_payments`, `bakeries`, `bands_orchestras`, `barber_and_beauty_shops`, `betting_casino_gambling`, `bicycle_shops`, `billiard_pool_establishments`, `boat_dealers`, `boat_rentals_and_leases`, `book_stores`, `books_periodicals_and_newspapers`, `bowling_alleys`, `bus_lines`, `business_secretarial_schools`, `buying_shopping_services`, `cable_satellite_and_other_pay_television_and_radio`, `camera_and_photographic_supply_stores`, `candy_nut_and_confectionery_stores`, `car_and_truck_dealers_new_used`, `car_and_truck_dealers_used_only`, `car_rental_agencies`, `car_washes`, `carpentry_services`, `carpet_upholstery_cleaning`, `caterers`, `charitable_and_social_service_organizations_fundraising`, `chemicals_and_allied_products`, `child_care_services`, `childrens_and_infants_wear_stores`, `chiropodists_podiatrists`, `chiropractors`, `cigar_stores_and_stands`, `civic_social_fraternal_associations`, `cleaning_and_maintenance`, `clothing_rental`, `colleges_universities`, `commercial_equipment`, `commercial_footwear`, `commercial_photography_art_and_graphics`, `commuter_transport_and_ferries`, `computer_network_services`, `computer_programming`, `computer_repair`, `computer_software_stores`, `computers_peripherals_and_software`, `concrete_work_services`, `construction_materials`, `consulting_public_relations`, `correspondence_schools`, `cosmetic_stores`, `counseling_services`, `country_clubs`, `courier_services`, `court_costs`, `credit_reporting_agencies`, `cruise_lines`, `dairy_products_stores`, `dance_hall_studios_schools`, `dating_escort_services`, `dentists_orthodontists`, `department_stores`, `detective_agencies`, `digital_goods_applications`, `digital_goods_games`, `digital_goods_large_volume`, `digital_goods_media`, `direct_marketing_catalog_merchant`, `direct_marketing_combination_catalog_and_retail_merchant`, `direct_marketing_inbound_telemarketing`, `direct_marketing_insurance_services`, `direct_marketing_other`, `direct_marketing_outbound_telemarketing`, `direct_marketing_subscription`, `direct_marketing_travel`, `discount_stores`, `doctors`, `door_to_door_sales`, `drapery_window_covering_and_upholstery_stores`, `drinking_places`, `drug_stores_and_pharmacies`, `drugs_drug_proprietaries_and_druggist_sundries`, `dry_cleaners`, `durable_goods`, `duty_free_stores`, `eating_places_restaurants`, `educational_services`, `electric_razor_stores`, `electric_vehicle_charging`, `electrical_parts_and_equipment`, `electrical_services`, `electronics_repair_shops`, `electronics_stores`, `elementary_secondary_schools`, `emergency_services_gcas_visa_use_only`, `employment_temp_agencies`, `equipment_rental`, `exterminating_services`, `family_clothing_stores`, `fast_food_restaurants`, `financial_institutions`, `fines_government_administrative_entities`, `fireplace_fireplace_screens_and_accessories_stores`, `floor_covering_stores`, `florists`, `florists_supplies_nursery_stock_and_flowers`, `freezer_and_locker_meat_provisioners`, `fuel_dealers_non_automotive`, `funeral_services_crematories`, `furniture_home_furnishings_and_equipment_stores_except_appliances`, `furniture_repair_refinishing`, `furriers_and_fur_shops`, `general_services`, `gift_card_novelty_and_souvenir_shops`, `glass_paint_and_wallpaper_stores`, `glassware_crystal_stores`, `golf_courses_public`, `government_licensed_horse_dog_racing_us_region_only`, `government_licensed_online_casions_online_gambling_us_region_only`, `government_owned_lotteries_non_us_region`, `government_owned_lotteries_us_region_only`, `government_services`, `grocery_stores_supermarkets`, `hardware_equipment_and_supplies`, `hardware_stores`, `health_and_beauty_spas`, `hearing_aids_sales_and_supplies`, `heating_plumbing_a_c`, `hobby_toy_and_game_shops`, `home_supply_warehouse_stores`, `hospitals`, `hotels_motels_and_resorts`, `household_appliance_stores`, `industrial_supplies`, `information_retrieval_services`, `insurance_default`, `insurance_underwriting_premiums`, `intra_company_purchases`, `jewelry_stores_watches_clocks_and_silverware_stores`, `landscaping_services`, `laundries`, `laundry_cleaning_services`, `legal_services_attorneys`, `luggage_and_leather_goods_stores`, `lumber_building_materials_stores`, `manual_cash_disburse`, `marinas_service_and_supplies`, `marketplaces`, `masonry_stonework_and_plaster`, `massage_parlors`, `medical_and_dental_labs`, `medical_dental_ophthalmic_and_hospital_equipment_and_supplies`, `medical_services`, `membership_organizations`, `mens_and_boys_clothing_and_accessories_stores`, `mens_womens_clothing_stores`, `metal_service_centers`, `miscellaneous`, `miscellaneous_apparel_and_accessory_shops`, `miscellaneous_auto_dealers`, `miscellaneous_business_services`, `miscellaneous_food_stores`, `miscellaneous_general_merchandise`, `miscellaneous_general_services`, `miscellaneous_home_furnishing_specialty_stores`, `miscellaneous_publishing_and_printing`, `miscellaneous_recreation_services`, `miscellaneous_repair_shops`, `miscellaneous_specialty_retail`, `mobile_home_dealers`, `motion_picture_theaters`, `motor_freight_carriers_and_trucking`, `motor_homes_dealers`, `motor_vehicle_supplies_and_new_parts`, `motorcycle_shops_and_dealers`, `motorcycle_shops_dealers`, `music_stores_musical_instruments_pianos_and_sheet_music`, `news_dealers_and_newsstands`, `non_fi_money_orders`, `non_fi_stored_value_card_purchase_load`, `nondurable_goods`, `nurseries_lawn_and_garden_supply_stores`, `nursing_personal_care`, `office_and_commercial_furniture`, `opticians_eyeglasses`, `optometrists_ophthalmologist`, `orthopedic_goods_prosthetic_devices`, `osteopaths`, `package_stores_beer_wine_and_liquor`, `paints_varnishes_and_supplies`, `parking_lots_garages`, `passenger_railways`, `pawn_shops`, `pet_shops_pet_food_and_supplies`, `petroleum_and_petroleum_products`, `photo_developing`, `photographic_photocopy_microfilm_equipment_and_supplies`, `photographic_studios`, `picture_video_production`, `piece_goods_notions_and_other_dry_goods`, `plumbing_heating_equipment_and_supplies`, `political_organizations`, `postal_services_government_only`, `precious_stones_and_metals_watches_and_jewelry`, `professional_services`, `public_warehousing_and_storage`, `quick_copy_repro_and_blueprint`, `railroads`, `real_estate_agents_and_managers_rentals`, `record_stores`, `recreational_vehicle_rentals`, `religious_goods_stores`, `religious_organizations`, `roofing_siding_sheet_metal`, `secretarial_support_services`, `security_brokers_dealers`, `service_stations`, `sewing_needlework_fabric_and_piece_goods_stores`, `shoe_repair_hat_cleaning`, `shoe_stores`, `small_appliance_repair`, `snowmobile_dealers`, `special_trade_services`, `specialty_cleaning`, `sporting_goods_stores`, `sporting_recreation_camps`, `sports_and_riding_apparel_stores`, `sports_clubs_fields`, `stamp_and_coin_stores`, `stationary_office_supplies_printing_and_writing_paper`, `stationery_stores_office_and_school_supply_stores`, `swimming_pools_sales`, `t_ui_travel_germany`, `tailors_alterations`, `tax_payments_government_agencies`, `tax_preparation_services`, `taxicabs_limousines`, `telecommunication_equipment_and_telephone_sales`, `telecommunication_services`, `telegraph_services`, `tent_and_awning_shops`, `testing_laboratories`, `theatrical_ticket_agencies`, `timeshares`, `tire_retreading_and_repair`, `tolls_bridge_fees`, `tourist_attractions_and_exhibits`, `towing_services`, `trailer_parks_campgrounds`, `transportation_services`, `travel_agencies_tour_operators`, `truck_stop_iteration`, `truck_utility_trailer_rentals`, `typesetting_plate_making_and_related_services`, `typewriter_stores`, `u_s_federal_government_agencies_or_departments`, `uniforms_commercial_clothing`, `used_merchandise_and_secondhand_stores`, `utilities`, `variety_stores`, `veterinary_services`, `video_amusement_game_supplies`, `video_game_arcades`, `video_tape_rental_stores`, `vocational_trade_schools`, `watch_jewelry_repair`, `welding_repair`, `wholesale_clubs`, `wig_and_toupee_stores`, `wires_money_orders`, `womens_accessory_and_specialty_shops`, `womens_ready_to_wear_stores`, `wrecking_and_salvage_yards` |  |  |
| `spending_controls.blocked_merchant_countries` | array of string |  |  |
| `spending_controls.spending_limits` | array of object |  |  |
| `spending_controls.spending_limits[].amount` | integer | yes |  |
| `spending_controls.spending_limits[].categories` | array of enum: `ac_refrigeration_repair`, `accounting_bookkeeping_services`, `advertising_services`, `agricultural_cooperative`, `airlines_air_carriers`, `airports_flying_fields`, `ambulance_services`, `amusement_parks_carnivals`, `antique_reproductions`, `antique_shops`, `aquariums`, `architectural_surveying_services`, `art_dealers_and_galleries`, `artists_supply_and_craft_shops`, `auto_and_home_supply_stores`, `auto_body_repair_shops`, `auto_paint_shops`, `auto_service_shops`, `automated_cash_disburse`, `automated_fuel_dispensers`, `automobile_associations`, `automotive_parts_and_accessories_stores`, `automotive_tire_stores`, `bail_and_bond_payments`, `bakeries`, `bands_orchestras`, `barber_and_beauty_shops`, `betting_casino_gambling`, `bicycle_shops`, `billiard_pool_establishments`, `boat_dealers`, `boat_rentals_and_leases`, `book_stores`, `books_periodicals_and_newspapers`, `bowling_alleys`, `bus_lines`, `business_secretarial_schools`, `buying_shopping_services`, `cable_satellite_and_other_pay_television_and_radio`, `camera_and_photographic_supply_stores`, `candy_nut_and_confectionery_stores`, `car_and_truck_dealers_new_used`, `car_and_truck_dealers_used_only`, `car_rental_agencies`, `car_washes`, `carpentry_services`, `carpet_upholstery_cleaning`, `caterers`, `charitable_and_social_service_organizations_fundraising`, `chemicals_and_allied_products`, `child_care_services`, `childrens_and_infants_wear_stores`, `chiropodists_podiatrists`, `chiropractors`, `cigar_stores_and_stands`, `civic_social_fraternal_associations`, `cleaning_and_maintenance`, `clothing_rental`, `colleges_universities`, `commercial_equipment`, `commercial_footwear`, `commercial_photography_art_and_graphics`, `commuter_transport_and_ferries`, `computer_network_services`, `computer_programming`, `computer_repair`, `computer_software_stores`, `computers_peripherals_and_software`, `concrete_work_services`, `construction_materials`, `consulting_public_relations`, `correspondence_schools`, `cosmetic_stores`, `counseling_services`, `country_clubs`, `courier_services`, `court_costs`, `credit_reporting_agencies`, `cruise_lines`, `dairy_products_stores`, `dance_hall_studios_schools`, `dating_escort_services`, `dentists_orthodontists`, `department_stores`, `detective_agencies`, `digital_goods_applications`, `digital_goods_games`, `digital_goods_large_volume`, `digital_goods_media`, `direct_marketing_catalog_merchant`, `direct_marketing_combination_catalog_and_retail_merchant`, `direct_marketing_inbound_telemarketing`, `direct_marketing_insurance_services`, `direct_marketing_other`, `direct_marketing_outbound_telemarketing`, `direct_marketing_subscription`, `direct_marketing_travel`, `discount_stores`, `doctors`, `door_to_door_sales`, `drapery_window_covering_and_upholstery_stores`, `drinking_places`, `drug_stores_and_pharmacies`, `drugs_drug_proprietaries_and_druggist_sundries`, `dry_cleaners`, `durable_goods`, `duty_free_stores`, `eating_places_restaurants`, `educational_services`, `electric_razor_stores`, `electric_vehicle_charging`, `electrical_parts_and_equipment`, `electrical_services`, `electronics_repair_shops`, `electronics_stores`, `elementary_secondary_schools`, `emergency_services_gcas_visa_use_only`, `employment_temp_agencies`, `equipment_rental`, `exterminating_services`, `family_clothing_stores`, `fast_food_restaurants`, `financial_institutions`, `fines_government_administrative_entities`, `fireplace_fireplace_screens_and_accessories_stores`, `floor_covering_stores`, `florists`, `florists_supplies_nursery_stock_and_flowers`, `freezer_and_locker_meat_provisioners`, `fuel_dealers_non_automotive`, `funeral_services_crematories`, `furniture_home_furnishings_and_equipment_stores_except_appliances`, `furniture_repair_refinishing`, `furriers_and_fur_shops`, `general_services`, `gift_card_novelty_and_souvenir_shops`, `glass_paint_and_wallpaper_stores`, `glassware_crystal_stores`, `golf_courses_public`, `government_licensed_horse_dog_racing_us_region_only`, `government_licensed_online_casions_online_gambling_us_region_only`, `government_owned_lotteries_non_us_region`, `government_owned_lotteries_us_region_only`, `government_services`, `grocery_stores_supermarkets`, `hardware_equipment_and_supplies`, `hardware_stores`, `health_and_beauty_spas`, `hearing_aids_sales_and_supplies`, `heating_plumbing_a_c`, `hobby_toy_and_game_shops`, `home_supply_warehouse_stores`, `hospitals`, `hotels_motels_and_resorts`, `household_appliance_stores`, `industrial_supplies`, `information_retrieval_services`, `insurance_default`, `insurance_underwriting_premiums`, `intra_company_purchases`, `jewelry_stores_watches_clocks_and_silverware_stores`, `landscaping_services`, `laundries`, `laundry_cleaning_services`, `legal_services_attorneys`, `luggage_and_leather_goods_stores`, `lumber_building_materials_stores`, `manual_cash_disburse`, `marinas_service_and_supplies`, `marketplaces`, `masonry_stonework_and_plaster`, `massage_parlors`, `medical_and_dental_labs`, `medical_dental_ophthalmic_and_hospital_equipment_and_supplies`, `medical_services`, `membership_organizations`, `mens_and_boys_clothing_and_accessories_stores`, `mens_womens_clothing_stores`, `metal_service_centers`, `miscellaneous`, `miscellaneous_apparel_and_accessory_shops`, `miscellaneous_auto_dealers`, `miscellaneous_business_services`, `miscellaneous_food_stores`, `miscellaneous_general_merchandise`, `miscellaneous_general_services`, `miscellaneous_home_furnishing_specialty_stores`, `miscellaneous_publishing_and_printing`, `miscellaneous_recreation_services`, `miscellaneous_repair_shops`, `miscellaneous_specialty_retail`, `mobile_home_dealers`, `motion_picture_theaters`, `motor_freight_carriers_and_trucking`, `motor_homes_dealers`, `motor_vehicle_supplies_and_new_parts`, `motorcycle_shops_and_dealers`, `motorcycle_shops_dealers`, `music_stores_musical_instruments_pianos_and_sheet_music`, `news_dealers_and_newsstands`, `non_fi_money_orders`, `non_fi_stored_value_card_purchase_load`, `nondurable_goods`, `nurseries_lawn_and_garden_supply_stores`, `nursing_personal_care`, `office_and_commercial_furniture`, `opticians_eyeglasses`, `optometrists_ophthalmologist`, `orthopedic_goods_prosthetic_devices`, `osteopaths`, `package_stores_beer_wine_and_liquor`, `paints_varnishes_and_supplies`, `parking_lots_garages`, `passenger_railways`, `pawn_shops`, `pet_shops_pet_food_and_supplies`, `petroleum_and_petroleum_products`, `photo_developing`, `photographic_photocopy_microfilm_equipment_and_supplies`, `photographic_studios`, `picture_video_production`, `piece_goods_notions_and_other_dry_goods`, `plumbing_heating_equipment_and_supplies`, `political_organizations`, `postal_services_government_only`, `precious_stones_and_metals_watches_and_jewelry`, `professional_services`, `public_warehousing_and_storage`, `quick_copy_repro_and_blueprint`, `railroads`, `real_estate_agents_and_managers_rentals`, `record_stores`, `recreational_vehicle_rentals`, `religious_goods_stores`, `religious_organizations`, `roofing_siding_sheet_metal`, `secretarial_support_services`, `security_brokers_dealers`, `service_stations`, `sewing_needlework_fabric_and_piece_goods_stores`, `shoe_repair_hat_cleaning`, `shoe_stores`, `small_appliance_repair`, `snowmobile_dealers`, `special_trade_services`, `specialty_cleaning`, `sporting_goods_stores`, `sporting_recreation_camps`, `sports_and_riding_apparel_stores`, `sports_clubs_fields`, `stamp_and_coin_stores`, `stationary_office_supplies_printing_and_writing_paper`, `stationery_stores_office_and_school_supply_stores`, `swimming_pools_sales`, `t_ui_travel_germany`, `tailors_alterations`, `tax_payments_government_agencies`, `tax_preparation_services`, `taxicabs_limousines`, `telecommunication_equipment_and_telephone_sales`, `telecommunication_services`, `telegraph_services`, `tent_and_awning_shops`, `testing_laboratories`, `theatrical_ticket_agencies`, `timeshares`, `tire_retreading_and_repair`, `tolls_bridge_fees`, `tourist_attractions_and_exhibits`, `towing_services`, `trailer_parks_campgrounds`, `transportation_services`, `travel_agencies_tour_operators`, `truck_stop_iteration`, `truck_utility_trailer_rentals`, `typesetting_plate_making_and_related_services`, `typewriter_stores`, `u_s_federal_government_agencies_or_departments`, `uniforms_commercial_clothing`, `used_merchandise_and_secondhand_stores`, `utilities`, `variety_stores`, `veterinary_services`, `video_amusement_game_supplies`, `video_game_arcades`, `video_tape_rental_stores`, `vocational_trade_schools`, `watch_jewelry_repair`, `welding_repair`, `wholesale_clubs`, `wig_and_toupee_stores`, `wires_money_orders`, `womens_accessory_and_specialty_shops`, `womens_ready_to_wear_stores`, `wrecking_and_salvage_yards` |  |  |
| `spending_controls.spending_limits[].interval` | enum: `all_time`, `daily`, `monthly`, `per_authorization`, `weekly`, `yearly` | yes |  |
| `spending_controls.spending_limits_currency` | string |  |  |
| `status` | enum: `active`, `inactive` |  | Specifies whether to permit authorizations on this cardholder's cards. |

Returns: `issuing.cardholder`

## GET /v1/issuing/cards

operationId: `GetIssuingCards`

Returns a list of Issuing `Card` objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `cardholder` | string |  | Only return cards belonging to the Cardholder with the provided ID. |
| `created` | object or integer |  | Only return cards that were issued during the given date interval. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `exp_month` | integer |  | Only return cards that have the given expiration month. |
| `exp_year` | integer |  | Only return cards that have the given expiration year. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `last4` | string |  | Only return cards that have the given last four digits. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `personalization_design` | string |  |  |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `status` | enum: `active`, `canceled`, `inactive` |  | Only return cards that have the given status. One of `active`, `inactive`, or `canceled`. |
| `type` | enum: `physical`, `virtual` |  | Only return cards that have the given type. One of `virtual` or `physical`. |

Returns: object

## POST /v1/issuing/cards

operationId: `PostIssuingCards`

Creates an Issuing `Card` object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `cardholder` | string |  | The [Cardholder](https://stripe.com/docs/api#issuing_cardholder_object) object with which the card will be associated. |
| `currency` | string | yes | The currency for the card. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `financial_account` | string |  |  |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `personalization_design` | string |  | The personalization design object belonging to this card. |
| `pin` | object |  | The desired PIN for this card. |
| `pin.encrypted_number` | string |  |  |
| `replacement_for` | string |  | The card this is meant to be a replacement for (if any). |
| `replacement_reason` | enum: `damaged`, `expired`, `lost`, `stolen` |  | If `replacement_for` is specified, this should indicate why that card is being replaced. |
| `second_line` | string or "" (to unset) |  | The second line to print on the card. |
| `shipping` | object |  | The address where the card will be shipped. |
| `shipping.address` | object | yes |  |
| `shipping.address.city` | string | yes |  |
| `shipping.address.country` | string | yes |  |
| `shipping.address.line1` | string | yes |  |
| `shipping.address.line2` | string |  |  |
| `shipping.address.postal_code` | string | yes |  |
| `shipping.address.state` | string |  |  |
| `shipping.customs` | object |  |  |
| `shipping.customs.eori_number` | string |  |  |
| `shipping.name` | string | yes |  |
| `shipping.phone_number` | string |  |  |
| `shipping.require_signature` | boolean |  |  |
| `shipping.service` | enum: `express`, `priority`, `standard` |  |  |
| `shipping.type` | enum: `bulk`, `individual` |  |  |
| `spending_controls` | object |  | Rules that control spending for this card. Refer to our [documentation](https://stripe.com/docs/issuing/controls/spending-controls) for more details. |
| `spending_controls.allowed_categories` | array of enum: `ac_refrigeration_repair`, `accounting_bookkeeping_services`, `advertising_services`, `agricultural_cooperative`, `airlines_air_carriers`, `airports_flying_fields`, `ambulance_services`, `amusement_parks_carnivals`, `antique_reproductions`, `antique_shops`, `aquariums`, `architectural_surveying_services`, `art_dealers_and_galleries`, `artists_supply_and_craft_shops`, `auto_and_home_supply_stores`, `auto_body_repair_shops`, `auto_paint_shops`, `auto_service_shops`, `automated_cash_disburse`, `automated_fuel_dispensers`, `automobile_associations`, `automotive_parts_and_accessories_stores`, `automotive_tire_stores`, `bail_and_bond_payments`, `bakeries`, `bands_orchestras`, `barber_and_beauty_shops`, `betting_casino_gambling`, `bicycle_shops`, `billiard_pool_establishments`, `boat_dealers`, `boat_rentals_and_leases`, `book_stores`, `books_periodicals_and_newspapers`, `bowling_alleys`, `bus_lines`, `business_secretarial_schools`, `buying_shopping_services`, `cable_satellite_and_other_pay_television_and_radio`, `camera_and_photographic_supply_stores`, `candy_nut_and_confectionery_stores`, `car_and_truck_dealers_new_used`, `car_and_truck_dealers_used_only`, `car_rental_agencies`, `car_washes`, `carpentry_services`, `carpet_upholstery_cleaning`, `caterers`, `charitable_and_social_service_organizations_fundraising`, `chemicals_and_allied_products`, `child_care_services`, `childrens_and_infants_wear_stores`, `chiropodists_podiatrists`, `chiropractors`, `cigar_stores_and_stands`, `civic_social_fraternal_associations`, `cleaning_and_maintenance`, `clothing_rental`, `colleges_universities`, `commercial_equipment`, `commercial_footwear`, `commercial_photography_art_and_graphics`, `commuter_transport_and_ferries`, `computer_network_services`, `computer_programming`, `computer_repair`, `computer_software_stores`, `computers_peripherals_and_software`, `concrete_work_services`, `construction_materials`, `consulting_public_relations`, `correspondence_schools`, `cosmetic_stores`, `counseling_services`, `country_clubs`, `courier_services`, `court_costs`, `credit_reporting_agencies`, `cruise_lines`, `dairy_products_stores`, `dance_hall_studios_schools`, `dating_escort_services`, `dentists_orthodontists`, `department_stores`, `detective_agencies`, `digital_goods_applications`, `digital_goods_games`, `digital_goods_large_volume`, `digital_goods_media`, `direct_marketing_catalog_merchant`, `direct_marketing_combination_catalog_and_retail_merchant`, `direct_marketing_inbound_telemarketing`, `direct_marketing_insurance_services`, `direct_marketing_other`, `direct_marketing_outbound_telemarketing`, `direct_marketing_subscription`, `direct_marketing_travel`, `discount_stores`, `doctors`, `door_to_door_sales`, `drapery_window_covering_and_upholstery_stores`, `drinking_places`, `drug_stores_and_pharmacies`, `drugs_drug_proprietaries_and_druggist_sundries`, `dry_cleaners`, `durable_goods`, `duty_free_stores`, `eating_places_restaurants`, `educational_services`, `electric_razor_stores`, `electric_vehicle_charging`, `electrical_parts_and_equipment`, `electrical_services`, `electronics_repair_shops`, `electronics_stores`, `elementary_secondary_schools`, `emergency_services_gcas_visa_use_only`, `employment_temp_agencies`, `equipment_rental`, `exterminating_services`, `family_clothing_stores`, `fast_food_restaurants`, `financial_institutions`, `fines_government_administrative_entities`, `fireplace_fireplace_screens_and_accessories_stores`, `floor_covering_stores`, `florists`, `florists_supplies_nursery_stock_and_flowers`, `freezer_and_locker_meat_provisioners`, `fuel_dealers_non_automotive`, `funeral_services_crematories`, `furniture_home_furnishings_and_equipment_stores_except_appliances`, `furniture_repair_refinishing`, `furriers_and_fur_shops`, `general_services`, `gift_card_novelty_and_souvenir_shops`, `glass_paint_and_wallpaper_stores`, `glassware_crystal_stores`, `golf_courses_public`, `government_licensed_horse_dog_racing_us_region_only`, `government_licensed_online_casions_online_gambling_us_region_only`, `government_owned_lotteries_non_us_region`, `government_owned_lotteries_us_region_only`, `government_services`, `grocery_stores_supermarkets`, `hardware_equipment_and_supplies`, `hardware_stores`, `health_and_beauty_spas`, `hearing_aids_sales_and_supplies`, `heating_plumbing_a_c`, `hobby_toy_and_game_shops`, `home_supply_warehouse_stores`, `hospitals`, `hotels_motels_and_resorts`, `household_appliance_stores`, `industrial_supplies`, `information_retrieval_services`, `insurance_default`, `insurance_underwriting_premiums`, `intra_company_purchases`, `jewelry_stores_watches_clocks_and_silverware_stores`, `landscaping_services`, `laundries`, `laundry_cleaning_services`, `legal_services_attorneys`, `luggage_and_leather_goods_stores`, `lumber_building_materials_stores`, `manual_cash_disburse`, `marinas_service_and_supplies`, `marketplaces`, `masonry_stonework_and_plaster`, `massage_parlors`, `medical_and_dental_labs`, `medical_dental_ophthalmic_and_hospital_equipment_and_supplies`, `medical_services`, `membership_organizations`, `mens_and_boys_clothing_and_accessories_stores`, `mens_womens_clothing_stores`, `metal_service_centers`, `miscellaneous`, `miscellaneous_apparel_and_accessory_shops`, `miscellaneous_auto_dealers`, `miscellaneous_business_services`, `miscellaneous_food_stores`, `miscellaneous_general_merchandise`, `miscellaneous_general_services`, `miscellaneous_home_furnishing_specialty_stores`, `miscellaneous_publishing_and_printing`, `miscellaneous_recreation_services`, `miscellaneous_repair_shops`, `miscellaneous_specialty_retail`, `mobile_home_dealers`, `motion_picture_theaters`, `motor_freight_carriers_and_trucking`, `motor_homes_dealers`, `motor_vehicle_supplies_and_new_parts`, `motorcycle_shops_and_dealers`, `motorcycle_shops_dealers`, `music_stores_musical_instruments_pianos_and_sheet_music`, `news_dealers_and_newsstands`, `non_fi_money_orders`, `non_fi_stored_value_card_purchase_load`, `nondurable_goods`, `nurseries_lawn_and_garden_supply_stores`, `nursing_personal_care`, `office_and_commercial_furniture`, `opticians_eyeglasses`, `optometrists_ophthalmologist`, `orthopedic_goods_prosthetic_devices`, `osteopaths`, `package_stores_beer_wine_and_liquor`, `paints_varnishes_and_supplies`, `parking_lots_garages`, `passenger_railways`, `pawn_shops`, `pet_shops_pet_food_and_supplies`, `petroleum_and_petroleum_products`, `photo_developing`, `photographic_photocopy_microfilm_equipment_and_supplies`, `photographic_studios`, `picture_video_production`, `piece_goods_notions_and_other_dry_goods`, `plumbing_heating_equipment_and_supplies`, `political_organizations`, `postal_services_government_only`, `precious_stones_and_metals_watches_and_jewelry`, `professional_services`, `public_warehousing_and_storage`, `quick_copy_repro_and_blueprint`, `railroads`, `real_estate_agents_and_managers_rentals`, `record_stores`, `recreational_vehicle_rentals`, `religious_goods_stores`, `religious_organizations`, `roofing_siding_sheet_metal`, `secretarial_support_services`, `security_brokers_dealers`, `service_stations`, `sewing_needlework_fabric_and_piece_goods_stores`, `shoe_repair_hat_cleaning`, `shoe_stores`, `small_appliance_repair`, `snowmobile_dealers`, `special_trade_services`, `specialty_cleaning`, `sporting_goods_stores`, `sporting_recreation_camps`, `sports_and_riding_apparel_stores`, `sports_clubs_fields`, `stamp_and_coin_stores`, `stationary_office_supplies_printing_and_writing_paper`, `stationery_stores_office_and_school_supply_stores`, `swimming_pools_sales`, `t_ui_travel_germany`, `tailors_alterations`, `tax_payments_government_agencies`, `tax_preparation_services`, `taxicabs_limousines`, `telecommunication_equipment_and_telephone_sales`, `telecommunication_services`, `telegraph_services`, `tent_and_awning_shops`, `testing_laboratories`, `theatrical_ticket_agencies`, `timeshares`, `tire_retreading_and_repair`, `tolls_bridge_fees`, `tourist_attractions_and_exhibits`, `towing_services`, `trailer_parks_campgrounds`, `transportation_services`, `travel_agencies_tour_operators`, `truck_stop_iteration`, `truck_utility_trailer_rentals`, `typesetting_plate_making_and_related_services`, `typewriter_stores`, `u_s_federal_government_agencies_or_departments`, `uniforms_commercial_clothing`, `used_merchandise_and_secondhand_stores`, `utilities`, `variety_stores`, `veterinary_services`, `video_amusement_game_supplies`, `video_game_arcades`, `video_tape_rental_stores`, `vocational_trade_schools`, `watch_jewelry_repair`, `welding_repair`, `wholesale_clubs`, `wig_and_toupee_stores`, `wires_money_orders`, `womens_accessory_and_specialty_shops`, `womens_ready_to_wear_stores`, `wrecking_and_salvage_yards` |  |  |
| `spending_controls.allowed_merchant_countries` | array of string |  |  |
| `spending_controls.blocked_categories` | array of enum: `ac_refrigeration_repair`, `accounting_bookkeeping_services`, `advertising_services`, `agricultural_cooperative`, `airlines_air_carriers`, `airports_flying_fields`, `ambulance_services`, `amusement_parks_carnivals`, `antique_reproductions`, `antique_shops`, `aquariums`, `architectural_surveying_services`, `art_dealers_and_galleries`, `artists_supply_and_craft_shops`, `auto_and_home_supply_stores`, `auto_body_repair_shops`, `auto_paint_shops`, `auto_service_shops`, `automated_cash_disburse`, `automated_fuel_dispensers`, `automobile_associations`, `automotive_parts_and_accessories_stores`, `automotive_tire_stores`, `bail_and_bond_payments`, `bakeries`, `bands_orchestras`, `barber_and_beauty_shops`, `betting_casino_gambling`, `bicycle_shops`, `billiard_pool_establishments`, `boat_dealers`, `boat_rentals_and_leases`, `book_stores`, `books_periodicals_and_newspapers`, `bowling_alleys`, `bus_lines`, `business_secretarial_schools`, `buying_shopping_services`, `cable_satellite_and_other_pay_television_and_radio`, `camera_and_photographic_supply_stores`, `candy_nut_and_confectionery_stores`, `car_and_truck_dealers_new_used`, `car_and_truck_dealers_used_only`, `car_rental_agencies`, `car_washes`, `carpentry_services`, `carpet_upholstery_cleaning`, `caterers`, `charitable_and_social_service_organizations_fundraising`, `chemicals_and_allied_products`, `child_care_services`, `childrens_and_infants_wear_stores`, `chiropodists_podiatrists`, `chiropractors`, `cigar_stores_and_stands`, `civic_social_fraternal_associations`, `cleaning_and_maintenance`, `clothing_rental`, `colleges_universities`, `commercial_equipment`, `commercial_footwear`, `commercial_photography_art_and_graphics`, `commuter_transport_and_ferries`, `computer_network_services`, `computer_programming`, `computer_repair`, `computer_software_stores`, `computers_peripherals_and_software`, `concrete_work_services`, `construction_materials`, `consulting_public_relations`, `correspondence_schools`, `cosmetic_stores`, `counseling_services`, `country_clubs`, `courier_services`, `court_costs`, `credit_reporting_agencies`, `cruise_lines`, `dairy_products_stores`, `dance_hall_studios_schools`, `dating_escort_services`, `dentists_orthodontists`, `department_stores`, `detective_agencies`, `digital_goods_applications`, `digital_goods_games`, `digital_goods_large_volume`, `digital_goods_media`, `direct_marketing_catalog_merchant`, `direct_marketing_combination_catalog_and_retail_merchant`, `direct_marketing_inbound_telemarketing`, `direct_marketing_insurance_services`, `direct_marketing_other`, `direct_marketing_outbound_telemarketing`, `direct_marketing_subscription`, `direct_marketing_travel`, `discount_stores`, `doctors`, `door_to_door_sales`, `drapery_window_covering_and_upholstery_stores`, `drinking_places`, `drug_stores_and_pharmacies`, `drugs_drug_proprietaries_and_druggist_sundries`, `dry_cleaners`, `durable_goods`, `duty_free_stores`, `eating_places_restaurants`, `educational_services`, `electric_razor_stores`, `electric_vehicle_charging`, `electrical_parts_and_equipment`, `electrical_services`, `electronics_repair_shops`, `electronics_stores`, `elementary_secondary_schools`, `emergency_services_gcas_visa_use_only`, `employment_temp_agencies`, `equipment_rental`, `exterminating_services`, `family_clothing_stores`, `fast_food_restaurants`, `financial_institutions`, `fines_government_administrative_entities`, `fireplace_fireplace_screens_and_accessories_stores`, `floor_covering_stores`, `florists`, `florists_supplies_nursery_stock_and_flowers`, `freezer_and_locker_meat_provisioners`, `fuel_dealers_non_automotive`, `funeral_services_crematories`, `furniture_home_furnishings_and_equipment_stores_except_appliances`, `furniture_repair_refinishing`, `furriers_and_fur_shops`, `general_services`, `gift_card_novelty_and_souvenir_shops`, `glass_paint_and_wallpaper_stores`, `glassware_crystal_stores`, `golf_courses_public`, `government_licensed_horse_dog_racing_us_region_only`, `government_licensed_online_casions_online_gambling_us_region_only`, `government_owned_lotteries_non_us_region`, `government_owned_lotteries_us_region_only`, `government_services`, `grocery_stores_supermarkets`, `hardware_equipment_and_supplies`, `hardware_stores`, `health_and_beauty_spas`, `hearing_aids_sales_and_supplies`, `heating_plumbing_a_c`, `hobby_toy_and_game_shops`, `home_supply_warehouse_stores`, `hospitals`, `hotels_motels_and_resorts`, `household_appliance_stores`, `industrial_supplies`, `information_retrieval_services`, `insurance_default`, `insurance_underwriting_premiums`, `intra_company_purchases`, `jewelry_stores_watches_clocks_and_silverware_stores`, `landscaping_services`, `laundries`, `laundry_cleaning_services`, `legal_services_attorneys`, `luggage_and_leather_goods_stores`, `lumber_building_materials_stores`, `manual_cash_disburse`, `marinas_service_and_supplies`, `marketplaces`, `masonry_stonework_and_plaster`, `massage_parlors`, `medical_and_dental_labs`, `medical_dental_ophthalmic_and_hospital_equipment_and_supplies`, `medical_services`, `membership_organizations`, `mens_and_boys_clothing_and_accessories_stores`, `mens_womens_clothing_stores`, `metal_service_centers`, `miscellaneous`, `miscellaneous_apparel_and_accessory_shops`, `miscellaneous_auto_dealers`, `miscellaneous_business_services`, `miscellaneous_food_stores`, `miscellaneous_general_merchandise`, `miscellaneous_general_services`, `miscellaneous_home_furnishing_specialty_stores`, `miscellaneous_publishing_and_printing`, `miscellaneous_recreation_services`, `miscellaneous_repair_shops`, `miscellaneous_specialty_retail`, `mobile_home_dealers`, `motion_picture_theaters`, `motor_freight_carriers_and_trucking`, `motor_homes_dealers`, `motor_vehicle_supplies_and_new_parts`, `motorcycle_shops_and_dealers`, `motorcycle_shops_dealers`, `music_stores_musical_instruments_pianos_and_sheet_music`, `news_dealers_and_newsstands`, `non_fi_money_orders`, `non_fi_stored_value_card_purchase_load`, `nondurable_goods`, `nurseries_lawn_and_garden_supply_stores`, `nursing_personal_care`, `office_and_commercial_furniture`, `opticians_eyeglasses`, `optometrists_ophthalmologist`, `orthopedic_goods_prosthetic_devices`, `osteopaths`, `package_stores_beer_wine_and_liquor`, `paints_varnishes_and_supplies`, `parking_lots_garages`, `passenger_railways`, `pawn_shops`, `pet_shops_pet_food_and_supplies`, `petroleum_and_petroleum_products`, `photo_developing`, `photographic_photocopy_microfilm_equipment_and_supplies`, `photographic_studios`, `picture_video_production`, `piece_goods_notions_and_other_dry_goods`, `plumbing_heating_equipment_and_supplies`, `political_organizations`, `postal_services_government_only`, `precious_stones_and_metals_watches_and_jewelry`, `professional_services`, `public_warehousing_and_storage`, `quick_copy_repro_and_blueprint`, `railroads`, `real_estate_agents_and_managers_rentals`, `record_stores`, `recreational_vehicle_rentals`, `religious_goods_stores`, `religious_organizations`, `roofing_siding_sheet_metal`, `secretarial_support_services`, `security_brokers_dealers`, `service_stations`, `sewing_needlework_fabric_and_piece_goods_stores`, `shoe_repair_hat_cleaning`, `shoe_stores`, `small_appliance_repair`, `snowmobile_dealers`, `special_trade_services`, `specialty_cleaning`, `sporting_goods_stores`, `sporting_recreation_camps`, `sports_and_riding_apparel_stores`, `sports_clubs_fields`, `stamp_and_coin_stores`, `stationary_office_supplies_printing_and_writing_paper`, `stationery_stores_office_and_school_supply_stores`, `swimming_pools_sales`, `t_ui_travel_germany`, `tailors_alterations`, `tax_payments_government_agencies`, `tax_preparation_services`, `taxicabs_limousines`, `telecommunication_equipment_and_telephone_sales`, `telecommunication_services`, `telegraph_services`, `tent_and_awning_shops`, `testing_laboratories`, `theatrical_ticket_agencies`, `timeshares`, `tire_retreading_and_repair`, `tolls_bridge_fees`, `tourist_attractions_and_exhibits`, `towing_services`, `trailer_parks_campgrounds`, `transportation_services`, `travel_agencies_tour_operators`, `truck_stop_iteration`, `truck_utility_trailer_rentals`, `typesetting_plate_making_and_related_services`, `typewriter_stores`, `u_s_federal_government_agencies_or_departments`, `uniforms_commercial_clothing`, `used_merchandise_and_secondhand_stores`, `utilities`, `variety_stores`, `veterinary_services`, `video_amusement_game_supplies`, `video_game_arcades`, `video_tape_rental_stores`, `vocational_trade_schools`, `watch_jewelry_repair`, `welding_repair`, `wholesale_clubs`, `wig_and_toupee_stores`, `wires_money_orders`, `womens_accessory_and_specialty_shops`, `womens_ready_to_wear_stores`, `wrecking_and_salvage_yards` |  |  |
| `spending_controls.blocked_merchant_countries` | array of string |  |  |
| `spending_controls.spending_limits` | array of object |  |  |
| `spending_controls.spending_limits[].amount` | integer | yes |  |
| `spending_controls.spending_limits[].categories` | array of enum: `ac_refrigeration_repair`, `accounting_bookkeeping_services`, `advertising_services`, `agricultural_cooperative`, `airlines_air_carriers`, `airports_flying_fields`, `ambulance_services`, `amusement_parks_carnivals`, `antique_reproductions`, `antique_shops`, `aquariums`, `architectural_surveying_services`, `art_dealers_and_galleries`, `artists_supply_and_craft_shops`, `auto_and_home_supply_stores`, `auto_body_repair_shops`, `auto_paint_shops`, `auto_service_shops`, `automated_cash_disburse`, `automated_fuel_dispensers`, `automobile_associations`, `automotive_parts_and_accessories_stores`, `automotive_tire_stores`, `bail_and_bond_payments`, `bakeries`, `bands_orchestras`, `barber_and_beauty_shops`, `betting_casino_gambling`, `bicycle_shops`, `billiard_pool_establishments`, `boat_dealers`, `boat_rentals_and_leases`, `book_stores`, `books_periodicals_and_newspapers`, `bowling_alleys`, `bus_lines`, `business_secretarial_schools`, `buying_shopping_services`, `cable_satellite_and_other_pay_television_and_radio`, `camera_and_photographic_supply_stores`, `candy_nut_and_confectionery_stores`, `car_and_truck_dealers_new_used`, `car_and_truck_dealers_used_only`, `car_rental_agencies`, `car_washes`, `carpentry_services`, `carpet_upholstery_cleaning`, `caterers`, `charitable_and_social_service_organizations_fundraising`, `chemicals_and_allied_products`, `child_care_services`, `childrens_and_infants_wear_stores`, `chiropodists_podiatrists`, `chiropractors`, `cigar_stores_and_stands`, `civic_social_fraternal_associations`, `cleaning_and_maintenance`, `clothing_rental`, `colleges_universities`, `commercial_equipment`, `commercial_footwear`, `commercial_photography_art_and_graphics`, `commuter_transport_and_ferries`, `computer_network_services`, `computer_programming`, `computer_repair`, `computer_software_stores`, `computers_peripherals_and_software`, `concrete_work_services`, `construction_materials`, `consulting_public_relations`, `correspondence_schools`, `cosmetic_stores`, `counseling_services`, `country_clubs`, `courier_services`, `court_costs`, `credit_reporting_agencies`, `cruise_lines`, `dairy_products_stores`, `dance_hall_studios_schools`, `dating_escort_services`, `dentists_orthodontists`, `department_stores`, `detective_agencies`, `digital_goods_applications`, `digital_goods_games`, `digital_goods_large_volume`, `digital_goods_media`, `direct_marketing_catalog_merchant`, `direct_marketing_combination_catalog_and_retail_merchant`, `direct_marketing_inbound_telemarketing`, `direct_marketing_insurance_services`, `direct_marketing_other`, `direct_marketing_outbound_telemarketing`, `direct_marketing_subscription`, `direct_marketing_travel`, `discount_stores`, `doctors`, `door_to_door_sales`, `drapery_window_covering_and_upholstery_stores`, `drinking_places`, `drug_stores_and_pharmacies`, `drugs_drug_proprietaries_and_druggist_sundries`, `dry_cleaners`, `durable_goods`, `duty_free_stores`, `eating_places_restaurants`, `educational_services`, `electric_razor_stores`, `electric_vehicle_charging`, `electrical_parts_and_equipment`, `electrical_services`, `electronics_repair_shops`, `electronics_stores`, `elementary_secondary_schools`, `emergency_services_gcas_visa_use_only`, `employment_temp_agencies`, `equipment_rental`, `exterminating_services`, `family_clothing_stores`, `fast_food_restaurants`, `financial_institutions`, `fines_government_administrative_entities`, `fireplace_fireplace_screens_and_accessories_stores`, `floor_covering_stores`, `florists`, `florists_supplies_nursery_stock_and_flowers`, `freezer_and_locker_meat_provisioners`, `fuel_dealers_non_automotive`, `funeral_services_crematories`, `furniture_home_furnishings_and_equipment_stores_except_appliances`, `furniture_repair_refinishing`, `furriers_and_fur_shops`, `general_services`, `gift_card_novelty_and_souvenir_shops`, `glass_paint_and_wallpaper_stores`, `glassware_crystal_stores`, `golf_courses_public`, `government_licensed_horse_dog_racing_us_region_only`, `government_licensed_online_casions_online_gambling_us_region_only`, `government_owned_lotteries_non_us_region`, `government_owned_lotteries_us_region_only`, `government_services`, `grocery_stores_supermarkets`, `hardware_equipment_and_supplies`, `hardware_stores`, `health_and_beauty_spas`, `hearing_aids_sales_and_supplies`, `heating_plumbing_a_c`, `hobby_toy_and_game_shops`, `home_supply_warehouse_stores`, `hospitals`, `hotels_motels_and_resorts`, `household_appliance_stores`, `industrial_supplies`, `information_retrieval_services`, `insurance_default`, `insurance_underwriting_premiums`, `intra_company_purchases`, `jewelry_stores_watches_clocks_and_silverware_stores`, `landscaping_services`, `laundries`, `laundry_cleaning_services`, `legal_services_attorneys`, `luggage_and_leather_goods_stores`, `lumber_building_materials_stores`, `manual_cash_disburse`, `marinas_service_and_supplies`, `marketplaces`, `masonry_stonework_and_plaster`, `massage_parlors`, `medical_and_dental_labs`, `medical_dental_ophthalmic_and_hospital_equipment_and_supplies`, `medical_services`, `membership_organizations`, `mens_and_boys_clothing_and_accessories_stores`, `mens_womens_clothing_stores`, `metal_service_centers`, `miscellaneous`, `miscellaneous_apparel_and_accessory_shops`, `miscellaneous_auto_dealers`, `miscellaneous_business_services`, `miscellaneous_food_stores`, `miscellaneous_general_merchandise`, `miscellaneous_general_services`, `miscellaneous_home_furnishing_specialty_stores`, `miscellaneous_publishing_and_printing`, `miscellaneous_recreation_services`, `miscellaneous_repair_shops`, `miscellaneous_specialty_retail`, `mobile_home_dealers`, `motion_picture_theaters`, `motor_freight_carriers_and_trucking`, `motor_homes_dealers`, `motor_vehicle_supplies_and_new_parts`, `motorcycle_shops_and_dealers`, `motorcycle_shops_dealers`, `music_stores_musical_instruments_pianos_and_sheet_music`, `news_dealers_and_newsstands`, `non_fi_money_orders`, `non_fi_stored_value_card_purchase_load`, `nondurable_goods`, `nurseries_lawn_and_garden_supply_stores`, `nursing_personal_care`, `office_and_commercial_furniture`, `opticians_eyeglasses`, `optometrists_ophthalmologist`, `orthopedic_goods_prosthetic_devices`, `osteopaths`, `package_stores_beer_wine_and_liquor`, `paints_varnishes_and_supplies`, `parking_lots_garages`, `passenger_railways`, `pawn_shops`, `pet_shops_pet_food_and_supplies`, `petroleum_and_petroleum_products`, `photo_developing`, `photographic_photocopy_microfilm_equipment_and_supplies`, `photographic_studios`, `picture_video_production`, `piece_goods_notions_and_other_dry_goods`, `plumbing_heating_equipment_and_supplies`, `political_organizations`, `postal_services_government_only`, `precious_stones_and_metals_watches_and_jewelry`, `professional_services`, `public_warehousing_and_storage`, `quick_copy_repro_and_blueprint`, `railroads`, `real_estate_agents_and_managers_rentals`, `record_stores`, `recreational_vehicle_rentals`, `religious_goods_stores`, `religious_organizations`, `roofing_siding_sheet_metal`, `secretarial_support_services`, `security_brokers_dealers`, `service_stations`, `sewing_needlework_fabric_and_piece_goods_stores`, `shoe_repair_hat_cleaning`, `shoe_stores`, `small_appliance_repair`, `snowmobile_dealers`, `special_trade_services`, `specialty_cleaning`, `sporting_goods_stores`, `sporting_recreation_camps`, `sports_and_riding_apparel_stores`, `sports_clubs_fields`, `stamp_and_coin_stores`, `stationary_office_supplies_printing_and_writing_paper`, `stationery_stores_office_and_school_supply_stores`, `swimming_pools_sales`, `t_ui_travel_germany`, `tailors_alterations`, `tax_payments_government_agencies`, `tax_preparation_services`, `taxicabs_limousines`, `telecommunication_equipment_and_telephone_sales`, `telecommunication_services`, `telegraph_services`, `tent_and_awning_shops`, `testing_laboratories`, `theatrical_ticket_agencies`, `timeshares`, `tire_retreading_and_repair`, `tolls_bridge_fees`, `tourist_attractions_and_exhibits`, `towing_services`, `trailer_parks_campgrounds`, `transportation_services`, `travel_agencies_tour_operators`, `truck_stop_iteration`, `truck_utility_trailer_rentals`, `typesetting_plate_making_and_related_services`, `typewriter_stores`, `u_s_federal_government_agencies_or_departments`, `uniforms_commercial_clothing`, `used_merchandise_and_secondhand_stores`, `utilities`, `variety_stores`, `veterinary_services`, `video_amusement_game_supplies`, `video_game_arcades`, `video_tape_rental_stores`, `vocational_trade_schools`, `watch_jewelry_repair`, `welding_repair`, `wholesale_clubs`, `wig_and_toupee_stores`, `wires_money_orders`, `womens_accessory_and_specialty_shops`, `womens_ready_to_wear_stores`, `wrecking_and_salvage_yards` |  |  |
| `spending_controls.spending_limits[].interval` | enum: `all_time`, `daily`, `monthly`, `per_authorization`, `weekly`, `yearly` | yes |  |
| `status` | enum: `active`, `inactive` |  | Whether authorizations can be approved on this card. May be blocked from activating cards depending on past-due Cardholder requirements. Defaults to `inactive`. |
| `type` | enum: `physical`, `virtual` | yes | The type of card to issue. Possible values are `physical` or `virtual`. |

Returns: `issuing.card`

## GET /v1/issuing/cards/{card}

operationId: `GetIssuingCardsCard`

Retrieves an Issuing `Card` object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `card (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `issuing.card`

## POST /v1/issuing/cards/{card}

operationId: `PostIssuingCardsCard`

Updates the specified Issuing `Card` object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `card (path)` | string | yes |  |
| `cancellation_reason` | enum: `lost`, `stolen` |  | Reason why the `status` of this card is `canceled`. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `personalization_design` | string |  |  |
| `pin` | object |  | The desired new PIN for this card. |
| `pin.encrypted_number` | string |  |  |
| `spending_controls` | object |  | Rules that control spending for this card. Refer to our [documentation](https://stripe.com/docs/issuing/controls/spending-controls) for more details. |
| `spending_controls.allowed_categories` | array of enum: `ac_refrigeration_repair`, `accounting_bookkeeping_services`, `advertising_services`, `agricultural_cooperative`, `airlines_air_carriers`, `airports_flying_fields`, `ambulance_services`, `amusement_parks_carnivals`, `antique_reproductions`, `antique_shops`, `aquariums`, `architectural_surveying_services`, `art_dealers_and_galleries`, `artists_supply_and_craft_shops`, `auto_and_home_supply_stores`, `auto_body_repair_shops`, `auto_paint_shops`, `auto_service_shops`, `automated_cash_disburse`, `automated_fuel_dispensers`, `automobile_associations`, `automotive_parts_and_accessories_stores`, `automotive_tire_stores`, `bail_and_bond_payments`, `bakeries`, `bands_orchestras`, `barber_and_beauty_shops`, `betting_casino_gambling`, `bicycle_shops`, `billiard_pool_establishments`, `boat_dealers`, `boat_rentals_and_leases`, `book_stores`, `books_periodicals_and_newspapers`, `bowling_alleys`, `bus_lines`, `business_secretarial_schools`, `buying_shopping_services`, `cable_satellite_and_other_pay_television_and_radio`, `camera_and_photographic_supply_stores`, `candy_nut_and_confectionery_stores`, `car_and_truck_dealers_new_used`, `car_and_truck_dealers_used_only`, `car_rental_agencies`, `car_washes`, `carpentry_services`, `carpet_upholstery_cleaning`, `caterers`, `charitable_and_social_service_organizations_fundraising`, `chemicals_and_allied_products`, `child_care_services`, `childrens_and_infants_wear_stores`, `chiropodists_podiatrists`, `chiropractors`, `cigar_stores_and_stands`, `civic_social_fraternal_associations`, `cleaning_and_maintenance`, `clothing_rental`, `colleges_universities`, `commercial_equipment`, `commercial_footwear`, `commercial_photography_art_and_graphics`, `commuter_transport_and_ferries`, `computer_network_services`, `computer_programming`, `computer_repair`, `computer_software_stores`, `computers_peripherals_and_software`, `concrete_work_services`, `construction_materials`, `consulting_public_relations`, `correspondence_schools`, `cosmetic_stores`, `counseling_services`, `country_clubs`, `courier_services`, `court_costs`, `credit_reporting_agencies`, `cruise_lines`, `dairy_products_stores`, `dance_hall_studios_schools`, `dating_escort_services`, `dentists_orthodontists`, `department_stores`, `detective_agencies`, `digital_goods_applications`, `digital_goods_games`, `digital_goods_large_volume`, `digital_goods_media`, `direct_marketing_catalog_merchant`, `direct_marketing_combination_catalog_and_retail_merchant`, `direct_marketing_inbound_telemarketing`, `direct_marketing_insurance_services`, `direct_marketing_other`, `direct_marketing_outbound_telemarketing`, `direct_marketing_subscription`, `direct_marketing_travel`, `discount_stores`, `doctors`, `door_to_door_sales`, `drapery_window_covering_and_upholstery_stores`, `drinking_places`, `drug_stores_and_pharmacies`, `drugs_drug_proprietaries_and_druggist_sundries`, `dry_cleaners`, `durable_goods`, `duty_free_stores`, `eating_places_restaurants`, `educational_services`, `electric_razor_stores`, `electric_vehicle_charging`, `electrical_parts_and_equipment`, `electrical_services`, `electronics_repair_shops`, `electronics_stores`, `elementary_secondary_schools`, `emergency_services_gcas_visa_use_only`, `employment_temp_agencies`, `equipment_rental`, `exterminating_services`, `family_clothing_stores`, `fast_food_restaurants`, `financial_institutions`, `fines_government_administrative_entities`, `fireplace_fireplace_screens_and_accessories_stores`, `floor_covering_stores`, `florists`, `florists_supplies_nursery_stock_and_flowers`, `freezer_and_locker_meat_provisioners`, `fuel_dealers_non_automotive`, `funeral_services_crematories`, `furniture_home_furnishings_and_equipment_stores_except_appliances`, `furniture_repair_refinishing`, `furriers_and_fur_shops`, `general_services`, `gift_card_novelty_and_souvenir_shops`, `glass_paint_and_wallpaper_stores`, `glassware_crystal_stores`, `golf_courses_public`, `government_licensed_horse_dog_racing_us_region_only`, `government_licensed_online_casions_online_gambling_us_region_only`, `government_owned_lotteries_non_us_region`, `government_owned_lotteries_us_region_only`, `government_services`, `grocery_stores_supermarkets`, `hardware_equipment_and_supplies`, `hardware_stores`, `health_and_beauty_spas`, `hearing_aids_sales_and_supplies`, `heating_plumbing_a_c`, `hobby_toy_and_game_shops`, `home_supply_warehouse_stores`, `hospitals`, `hotels_motels_and_resorts`, `household_appliance_stores`, `industrial_supplies`, `information_retrieval_services`, `insurance_default`, `insurance_underwriting_premiums`, `intra_company_purchases`, `jewelry_stores_watches_clocks_and_silverware_stores`, `landscaping_services`, `laundries`, `laundry_cleaning_services`, `legal_services_attorneys`, `luggage_and_leather_goods_stores`, `lumber_building_materials_stores`, `manual_cash_disburse`, `marinas_service_and_supplies`, `marketplaces`, `masonry_stonework_and_plaster`, `massage_parlors`, `medical_and_dental_labs`, `medical_dental_ophthalmic_and_hospital_equipment_and_supplies`, `medical_services`, `membership_organizations`, `mens_and_boys_clothing_and_accessories_stores`, `mens_womens_clothing_stores`, `metal_service_centers`, `miscellaneous`, `miscellaneous_apparel_and_accessory_shops`, `miscellaneous_auto_dealers`, `miscellaneous_business_services`, `miscellaneous_food_stores`, `miscellaneous_general_merchandise`, `miscellaneous_general_services`, `miscellaneous_home_furnishing_specialty_stores`, `miscellaneous_publishing_and_printing`, `miscellaneous_recreation_services`, `miscellaneous_repair_shops`, `miscellaneous_specialty_retail`, `mobile_home_dealers`, `motion_picture_theaters`, `motor_freight_carriers_and_trucking`, `motor_homes_dealers`, `motor_vehicle_supplies_and_new_parts`, `motorcycle_shops_and_dealers`, `motorcycle_shops_dealers`, `music_stores_musical_instruments_pianos_and_sheet_music`, `news_dealers_and_newsstands`, `non_fi_money_orders`, `non_fi_stored_value_card_purchase_load`, `nondurable_goods`, `nurseries_lawn_and_garden_supply_stores`, `nursing_personal_care`, `office_and_commercial_furniture`, `opticians_eyeglasses`, `optometrists_ophthalmologist`, `orthopedic_goods_prosthetic_devices`, `osteopaths`, `package_stores_beer_wine_and_liquor`, `paints_varnishes_and_supplies`, `parking_lots_garages`, `passenger_railways`, `pawn_shops`, `pet_shops_pet_food_and_supplies`, `petroleum_and_petroleum_products`, `photo_developing`, `photographic_photocopy_microfilm_equipment_and_supplies`, `photographic_studios`, `picture_video_production`, `piece_goods_notions_and_other_dry_goods`, `plumbing_heating_equipment_and_supplies`, `political_organizations`, `postal_services_government_only`, `precious_stones_and_metals_watches_and_jewelry`, `professional_services`, `public_warehousing_and_storage`, `quick_copy_repro_and_blueprint`, `railroads`, `real_estate_agents_and_managers_rentals`, `record_stores`, `recreational_vehicle_rentals`, `religious_goods_stores`, `religious_organizations`, `roofing_siding_sheet_metal`, `secretarial_support_services`, `security_brokers_dealers`, `service_stations`, `sewing_needlework_fabric_and_piece_goods_stores`, `shoe_repair_hat_cleaning`, `shoe_stores`, `small_appliance_repair`, `snowmobile_dealers`, `special_trade_services`, `specialty_cleaning`, `sporting_goods_stores`, `sporting_recreation_camps`, `sports_and_riding_apparel_stores`, `sports_clubs_fields`, `stamp_and_coin_stores`, `stationary_office_supplies_printing_and_writing_paper`, `stationery_stores_office_and_school_supply_stores`, `swimming_pools_sales`, `t_ui_travel_germany`, `tailors_alterations`, `tax_payments_government_agencies`, `tax_preparation_services`, `taxicabs_limousines`, `telecommunication_equipment_and_telephone_sales`, `telecommunication_services`, `telegraph_services`, `tent_and_awning_shops`, `testing_laboratories`, `theatrical_ticket_agencies`, `timeshares`, `tire_retreading_and_repair`, `tolls_bridge_fees`, `tourist_attractions_and_exhibits`, `towing_services`, `trailer_parks_campgrounds`, `transportation_services`, `travel_agencies_tour_operators`, `truck_stop_iteration`, `truck_utility_trailer_rentals`, `typesetting_plate_making_and_related_services`, `typewriter_stores`, `u_s_federal_government_agencies_or_departments`, `uniforms_commercial_clothing`, `used_merchandise_and_secondhand_stores`, `utilities`, `variety_stores`, `veterinary_services`, `video_amusement_game_supplies`, `video_game_arcades`, `video_tape_rental_stores`, `vocational_trade_schools`, `watch_jewelry_repair`, `welding_repair`, `wholesale_clubs`, `wig_and_toupee_stores`, `wires_money_orders`, `womens_accessory_and_specialty_shops`, `womens_ready_to_wear_stores`, `wrecking_and_salvage_yards` |  |  |
| `spending_controls.allowed_merchant_countries` | array of string |  |  |
| `spending_controls.blocked_categories` | array of enum: `ac_refrigeration_repair`, `accounting_bookkeeping_services`, `advertising_services`, `agricultural_cooperative`, `airlines_air_carriers`, `airports_flying_fields`, `ambulance_services`, `amusement_parks_carnivals`, `antique_reproductions`, `antique_shops`, `aquariums`, `architectural_surveying_services`, `art_dealers_and_galleries`, `artists_supply_and_craft_shops`, `auto_and_home_supply_stores`, `auto_body_repair_shops`, `auto_paint_shops`, `auto_service_shops`, `automated_cash_disburse`, `automated_fuel_dispensers`, `automobile_associations`, `automotive_parts_and_accessories_stores`, `automotive_tire_stores`, `bail_and_bond_payments`, `bakeries`, `bands_orchestras`, `barber_and_beauty_shops`, `betting_casino_gambling`, `bicycle_shops`, `billiard_pool_establishments`, `boat_dealers`, `boat_rentals_and_leases`, `book_stores`, `books_periodicals_and_newspapers`, `bowling_alleys`, `bus_lines`, `business_secretarial_schools`, `buying_shopping_services`, `cable_satellite_and_other_pay_television_and_radio`, `camera_and_photographic_supply_stores`, `candy_nut_and_confectionery_stores`, `car_and_truck_dealers_new_used`, `car_and_truck_dealers_used_only`, `car_rental_agencies`, `car_washes`, `carpentry_services`, `carpet_upholstery_cleaning`, `caterers`, `charitable_and_social_service_organizations_fundraising`, `chemicals_and_allied_products`, `child_care_services`, `childrens_and_infants_wear_stores`, `chiropodists_podiatrists`, `chiropractors`, `cigar_stores_and_stands`, `civic_social_fraternal_associations`, `cleaning_and_maintenance`, `clothing_rental`, `colleges_universities`, `commercial_equipment`, `commercial_footwear`, `commercial_photography_art_and_graphics`, `commuter_transport_and_ferries`, `computer_network_services`, `computer_programming`, `computer_repair`, `computer_software_stores`, `computers_peripherals_and_software`, `concrete_work_services`, `construction_materials`, `consulting_public_relations`, `correspondence_schools`, `cosmetic_stores`, `counseling_services`, `country_clubs`, `courier_services`, `court_costs`, `credit_reporting_agencies`, `cruise_lines`, `dairy_products_stores`, `dance_hall_studios_schools`, `dating_escort_services`, `dentists_orthodontists`, `department_stores`, `detective_agencies`, `digital_goods_applications`, `digital_goods_games`, `digital_goods_large_volume`, `digital_goods_media`, `direct_marketing_catalog_merchant`, `direct_marketing_combination_catalog_and_retail_merchant`, `direct_marketing_inbound_telemarketing`, `direct_marketing_insurance_services`, `direct_marketing_other`, `direct_marketing_outbound_telemarketing`, `direct_marketing_subscription`, `direct_marketing_travel`, `discount_stores`, `doctors`, `door_to_door_sales`, `drapery_window_covering_and_upholstery_stores`, `drinking_places`, `drug_stores_and_pharmacies`, `drugs_drug_proprietaries_and_druggist_sundries`, `dry_cleaners`, `durable_goods`, `duty_free_stores`, `eating_places_restaurants`, `educational_services`, `electric_razor_stores`, `electric_vehicle_charging`, `electrical_parts_and_equipment`, `electrical_services`, `electronics_repair_shops`, `electronics_stores`, `elementary_secondary_schools`, `emergency_services_gcas_visa_use_only`, `employment_temp_agencies`, `equipment_rental`, `exterminating_services`, `family_clothing_stores`, `fast_food_restaurants`, `financial_institutions`, `fines_government_administrative_entities`, `fireplace_fireplace_screens_and_accessories_stores`, `floor_covering_stores`, `florists`, `florists_supplies_nursery_stock_and_flowers`, `freezer_and_locker_meat_provisioners`, `fuel_dealers_non_automotive`, `funeral_services_crematories`, `furniture_home_furnishings_and_equipment_stores_except_appliances`, `furniture_repair_refinishing`, `furriers_and_fur_shops`, `general_services`, `gift_card_novelty_and_souvenir_shops`, `glass_paint_and_wallpaper_stores`, `glassware_crystal_stores`, `golf_courses_public`, `government_licensed_horse_dog_racing_us_region_only`, `government_licensed_online_casions_online_gambling_us_region_only`, `government_owned_lotteries_non_us_region`, `government_owned_lotteries_us_region_only`, `government_services`, `grocery_stores_supermarkets`, `hardware_equipment_and_supplies`, `hardware_stores`, `health_and_beauty_spas`, `hearing_aids_sales_and_supplies`, `heating_plumbing_a_c`, `hobby_toy_and_game_shops`, `home_supply_warehouse_stores`, `hospitals`, `hotels_motels_and_resorts`, `household_appliance_stores`, `industrial_supplies`, `information_retrieval_services`, `insurance_default`, `insurance_underwriting_premiums`, `intra_company_purchases`, `jewelry_stores_watches_clocks_and_silverware_stores`, `landscaping_services`, `laundries`, `laundry_cleaning_services`, `legal_services_attorneys`, `luggage_and_leather_goods_stores`, `lumber_building_materials_stores`, `manual_cash_disburse`, `marinas_service_and_supplies`, `marketplaces`, `masonry_stonework_and_plaster`, `massage_parlors`, `medical_and_dental_labs`, `medical_dental_ophthalmic_and_hospital_equipment_and_supplies`, `medical_services`, `membership_organizations`, `mens_and_boys_clothing_and_accessories_stores`, `mens_womens_clothing_stores`, `metal_service_centers`, `miscellaneous`, `miscellaneous_apparel_and_accessory_shops`, `miscellaneous_auto_dealers`, `miscellaneous_business_services`, `miscellaneous_food_stores`, `miscellaneous_general_merchandise`, `miscellaneous_general_services`, `miscellaneous_home_furnishing_specialty_stores`, `miscellaneous_publishing_and_printing`, `miscellaneous_recreation_services`, `miscellaneous_repair_shops`, `miscellaneous_specialty_retail`, `mobile_home_dealers`, `motion_picture_theaters`, `motor_freight_carriers_and_trucking`, `motor_homes_dealers`, `motor_vehicle_supplies_and_new_parts`, `motorcycle_shops_and_dealers`, `motorcycle_shops_dealers`, `music_stores_musical_instruments_pianos_and_sheet_music`, `news_dealers_and_newsstands`, `non_fi_money_orders`, `non_fi_stored_value_card_purchase_load`, `nondurable_goods`, `nurseries_lawn_and_garden_supply_stores`, `nursing_personal_care`, `office_and_commercial_furniture`, `opticians_eyeglasses`, `optometrists_ophthalmologist`, `orthopedic_goods_prosthetic_devices`, `osteopaths`, `package_stores_beer_wine_and_liquor`, `paints_varnishes_and_supplies`, `parking_lots_garages`, `passenger_railways`, `pawn_shops`, `pet_shops_pet_food_and_supplies`, `petroleum_and_petroleum_products`, `photo_developing`, `photographic_photocopy_microfilm_equipment_and_supplies`, `photographic_studios`, `picture_video_production`, `piece_goods_notions_and_other_dry_goods`, `plumbing_heating_equipment_and_supplies`, `political_organizations`, `postal_services_government_only`, `precious_stones_and_metals_watches_and_jewelry`, `professional_services`, `public_warehousing_and_storage`, `quick_copy_repro_and_blueprint`, `railroads`, `real_estate_agents_and_managers_rentals`, `record_stores`, `recreational_vehicle_rentals`, `religious_goods_stores`, `religious_organizations`, `roofing_siding_sheet_metal`, `secretarial_support_services`, `security_brokers_dealers`, `service_stations`, `sewing_needlework_fabric_and_piece_goods_stores`, `shoe_repair_hat_cleaning`, `shoe_stores`, `small_appliance_repair`, `snowmobile_dealers`, `special_trade_services`, `specialty_cleaning`, `sporting_goods_stores`, `sporting_recreation_camps`, `sports_and_riding_apparel_stores`, `sports_clubs_fields`, `stamp_and_coin_stores`, `stationary_office_supplies_printing_and_writing_paper`, `stationery_stores_office_and_school_supply_stores`, `swimming_pools_sales`, `t_ui_travel_germany`, `tailors_alterations`, `tax_payments_government_agencies`, `tax_preparation_services`, `taxicabs_limousines`, `telecommunication_equipment_and_telephone_sales`, `telecommunication_services`, `telegraph_services`, `tent_and_awning_shops`, `testing_laboratories`, `theatrical_ticket_agencies`, `timeshares`, `tire_retreading_and_repair`, `tolls_bridge_fees`, `tourist_attractions_and_exhibits`, `towing_services`, `trailer_parks_campgrounds`, `transportation_services`, `travel_agencies_tour_operators`, `truck_stop_iteration`, `truck_utility_trailer_rentals`, `typesetting_plate_making_and_related_services`, `typewriter_stores`, `u_s_federal_government_agencies_or_departments`, `uniforms_commercial_clothing`, `used_merchandise_and_secondhand_stores`, `utilities`, `variety_stores`, `veterinary_services`, `video_amusement_game_supplies`, `video_game_arcades`, `video_tape_rental_stores`, `vocational_trade_schools`, `watch_jewelry_repair`, `welding_repair`, `wholesale_clubs`, `wig_and_toupee_stores`, `wires_money_orders`, `womens_accessory_and_specialty_shops`, `womens_ready_to_wear_stores`, `wrecking_and_salvage_yards` |  |  |
| `spending_controls.blocked_merchant_countries` | array of string |  |  |
| `spending_controls.spending_limits` | array of object |  |  |
| `spending_controls.spending_limits[].amount` | integer | yes |  |
| `spending_controls.spending_limits[].categories` | array of enum: `ac_refrigeration_repair`, `accounting_bookkeeping_services`, `advertising_services`, `agricultural_cooperative`, `airlines_air_carriers`, `airports_flying_fields`, `ambulance_services`, `amusement_parks_carnivals`, `antique_reproductions`, `antique_shops`, `aquariums`, `architectural_surveying_services`, `art_dealers_and_galleries`, `artists_supply_and_craft_shops`, `auto_and_home_supply_stores`, `auto_body_repair_shops`, `auto_paint_shops`, `auto_service_shops`, `automated_cash_disburse`, `automated_fuel_dispensers`, `automobile_associations`, `automotive_parts_and_accessories_stores`, `automotive_tire_stores`, `bail_and_bond_payments`, `bakeries`, `bands_orchestras`, `barber_and_beauty_shops`, `betting_casino_gambling`, `bicycle_shops`, `billiard_pool_establishments`, `boat_dealers`, `boat_rentals_and_leases`, `book_stores`, `books_periodicals_and_newspapers`, `bowling_alleys`, `bus_lines`, `business_secretarial_schools`, `buying_shopping_services`, `cable_satellite_and_other_pay_television_and_radio`, `camera_and_photographic_supply_stores`, `candy_nut_and_confectionery_stores`, `car_and_truck_dealers_new_used`, `car_and_truck_dealers_used_only`, `car_rental_agencies`, `car_washes`, `carpentry_services`, `carpet_upholstery_cleaning`, `caterers`, `charitable_and_social_service_organizations_fundraising`, `chemicals_and_allied_products`, `child_care_services`, `childrens_and_infants_wear_stores`, `chiropodists_podiatrists`, `chiropractors`, `cigar_stores_and_stands`, `civic_social_fraternal_associations`, `cleaning_and_maintenance`, `clothing_rental`, `colleges_universities`, `commercial_equipment`, `commercial_footwear`, `commercial_photography_art_and_graphics`, `commuter_transport_and_ferries`, `computer_network_services`, `computer_programming`, `computer_repair`, `computer_software_stores`, `computers_peripherals_and_software`, `concrete_work_services`, `construction_materials`, `consulting_public_relations`, `correspondence_schools`, `cosmetic_stores`, `counseling_services`, `country_clubs`, `courier_services`, `court_costs`, `credit_reporting_agencies`, `cruise_lines`, `dairy_products_stores`, `dance_hall_studios_schools`, `dating_escort_services`, `dentists_orthodontists`, `department_stores`, `detective_agencies`, `digital_goods_applications`, `digital_goods_games`, `digital_goods_large_volume`, `digital_goods_media`, `direct_marketing_catalog_merchant`, `direct_marketing_combination_catalog_and_retail_merchant`, `direct_marketing_inbound_telemarketing`, `direct_marketing_insurance_services`, `direct_marketing_other`, `direct_marketing_outbound_telemarketing`, `direct_marketing_subscription`, `direct_marketing_travel`, `discount_stores`, `doctors`, `door_to_door_sales`, `drapery_window_covering_and_upholstery_stores`, `drinking_places`, `drug_stores_and_pharmacies`, `drugs_drug_proprietaries_and_druggist_sundries`, `dry_cleaners`, `durable_goods`, `duty_free_stores`, `eating_places_restaurants`, `educational_services`, `electric_razor_stores`, `electric_vehicle_charging`, `electrical_parts_and_equipment`, `electrical_services`, `electronics_repair_shops`, `electronics_stores`, `elementary_secondary_schools`, `emergency_services_gcas_visa_use_only`, `employment_temp_agencies`, `equipment_rental`, `exterminating_services`, `family_clothing_stores`, `fast_food_restaurants`, `financial_institutions`, `fines_government_administrative_entities`, `fireplace_fireplace_screens_and_accessories_stores`, `floor_covering_stores`, `florists`, `florists_supplies_nursery_stock_and_flowers`, `freezer_and_locker_meat_provisioners`, `fuel_dealers_non_automotive`, `funeral_services_crematories`, `furniture_home_furnishings_and_equipment_stores_except_appliances`, `furniture_repair_refinishing`, `furriers_and_fur_shops`, `general_services`, `gift_card_novelty_and_souvenir_shops`, `glass_paint_and_wallpaper_stores`, `glassware_crystal_stores`, `golf_courses_public`, `government_licensed_horse_dog_racing_us_region_only`, `government_licensed_online_casions_online_gambling_us_region_only`, `government_owned_lotteries_non_us_region`, `government_owned_lotteries_us_region_only`, `government_services`, `grocery_stores_supermarkets`, `hardware_equipment_and_supplies`, `hardware_stores`, `health_and_beauty_spas`, `hearing_aids_sales_and_supplies`, `heating_plumbing_a_c`, `hobby_toy_and_game_shops`, `home_supply_warehouse_stores`, `hospitals`, `hotels_motels_and_resorts`, `household_appliance_stores`, `industrial_supplies`, `information_retrieval_services`, `insurance_default`, `insurance_underwriting_premiums`, `intra_company_purchases`, `jewelry_stores_watches_clocks_and_silverware_stores`, `landscaping_services`, `laundries`, `laundry_cleaning_services`, `legal_services_attorneys`, `luggage_and_leather_goods_stores`, `lumber_building_materials_stores`, `manual_cash_disburse`, `marinas_service_and_supplies`, `marketplaces`, `masonry_stonework_and_plaster`, `massage_parlors`, `medical_and_dental_labs`, `medical_dental_ophthalmic_and_hospital_equipment_and_supplies`, `medical_services`, `membership_organizations`, `mens_and_boys_clothing_and_accessories_stores`, `mens_womens_clothing_stores`, `metal_service_centers`, `miscellaneous`, `miscellaneous_apparel_and_accessory_shops`, `miscellaneous_auto_dealers`, `miscellaneous_business_services`, `miscellaneous_food_stores`, `miscellaneous_general_merchandise`, `miscellaneous_general_services`, `miscellaneous_home_furnishing_specialty_stores`, `miscellaneous_publishing_and_printing`, `miscellaneous_recreation_services`, `miscellaneous_repair_shops`, `miscellaneous_specialty_retail`, `mobile_home_dealers`, `motion_picture_theaters`, `motor_freight_carriers_and_trucking`, `motor_homes_dealers`, `motor_vehicle_supplies_and_new_parts`, `motorcycle_shops_and_dealers`, `motorcycle_shops_dealers`, `music_stores_musical_instruments_pianos_and_sheet_music`, `news_dealers_and_newsstands`, `non_fi_money_orders`, `non_fi_stored_value_card_purchase_load`, `nondurable_goods`, `nurseries_lawn_and_garden_supply_stores`, `nursing_personal_care`, `office_and_commercial_furniture`, `opticians_eyeglasses`, `optometrists_ophthalmologist`, `orthopedic_goods_prosthetic_devices`, `osteopaths`, `package_stores_beer_wine_and_liquor`, `paints_varnishes_and_supplies`, `parking_lots_garages`, `passenger_railways`, `pawn_shops`, `pet_shops_pet_food_and_supplies`, `petroleum_and_petroleum_products`, `photo_developing`, `photographic_photocopy_microfilm_equipment_and_supplies`, `photographic_studios`, `picture_video_production`, `piece_goods_notions_and_other_dry_goods`, `plumbing_heating_equipment_and_supplies`, `political_organizations`, `postal_services_government_only`, `precious_stones_and_metals_watches_and_jewelry`, `professional_services`, `public_warehousing_and_storage`, `quick_copy_repro_and_blueprint`, `railroads`, `real_estate_agents_and_managers_rentals`, `record_stores`, `recreational_vehicle_rentals`, `religious_goods_stores`, `religious_organizations`, `roofing_siding_sheet_metal`, `secretarial_support_services`, `security_brokers_dealers`, `service_stations`, `sewing_needlework_fabric_and_piece_goods_stores`, `shoe_repair_hat_cleaning`, `shoe_stores`, `small_appliance_repair`, `snowmobile_dealers`, `special_trade_services`, `specialty_cleaning`, `sporting_goods_stores`, `sporting_recreation_camps`, `sports_and_riding_apparel_stores`, `sports_clubs_fields`, `stamp_and_coin_stores`, `stationary_office_supplies_printing_and_writing_paper`, `stationery_stores_office_and_school_supply_stores`, `swimming_pools_sales`, `t_ui_travel_germany`, `tailors_alterations`, `tax_payments_government_agencies`, `tax_preparation_services`, `taxicabs_limousines`, `telecommunication_equipment_and_telephone_sales`, `telecommunication_services`, `telegraph_services`, `tent_and_awning_shops`, `testing_laboratories`, `theatrical_ticket_agencies`, `timeshares`, `tire_retreading_and_repair`, `tolls_bridge_fees`, `tourist_attractions_and_exhibits`, `towing_services`, `trailer_parks_campgrounds`, `transportation_services`, `travel_agencies_tour_operators`, `truck_stop_iteration`, `truck_utility_trailer_rentals`, `typesetting_plate_making_and_related_services`, `typewriter_stores`, `u_s_federal_government_agencies_or_departments`, `uniforms_commercial_clothing`, `used_merchandise_and_secondhand_stores`, `utilities`, `variety_stores`, `veterinary_services`, `video_amusement_game_supplies`, `video_game_arcades`, `video_tape_rental_stores`, `vocational_trade_schools`, `watch_jewelry_repair`, `welding_repair`, `wholesale_clubs`, `wig_and_toupee_stores`, `wires_money_orders`, `womens_accessory_and_specialty_shops`, `womens_ready_to_wear_stores`, `wrecking_and_salvage_yards` |  |  |
| `spending_controls.spending_limits[].interval` | enum: `all_time`, `daily`, `monthly`, `per_authorization`, `weekly`, `yearly` | yes |  |
| `status` | enum: `active`, `canceled`, `inactive` |  | Dictates whether authorizations can be approved on this card. May be blocked from activating cards depending on past-due Cardholder requirements. Defaults to `inactive`. If this card is being canceled because it was lost or stolen, this information should be provided as `cancellation_reason`. |

Returns: `issuing.card`

## GET /v1/issuing/disputes

operationId: `GetIssuingDisputes`

Returns a list of Issuing `Dispute` objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | object or integer |  | Only return Issuing disputes that were created during the given date interval. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `status` | enum: `expired`, `lost`, `submitted`, `unsubmitted`, `won` |  | Select Issuing disputes with the given status. |
| `transaction` | string |  | Select the Issuing dispute for the given transaction. |

Returns: object

## POST /v1/issuing/disputes

operationId: `PostIssuingDisputes`

Creates an Issuing `Dispute` object. Individual pieces of evidence within the `evidence` object are optional at this point. Stripe only validates that required evidence is present during submission. Refer to [Dispute reasons and evidence](https://stripe.com/docs/issuing/purchases/disputes#dispute-reasons-and-evidence) for more details about evidence requirements.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer |  | The dispute amount in the card's currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). If not set, defaults to the full transaction amount. |
| `evidence` | object |  | Evidence provided for the dispute. |
| `evidence.canceled` | object or "" (to unset) |  |  |
| `evidence.canceled.additional_documentation` | string or "" (to unset) |  |  |
| `evidence.canceled.canceled_at` | timestamp (Unix seconds) or "" (to unset) |  |  |
| `evidence.canceled.cancellation_policy_provided` | boolean or "" (to unset) |  |  |
| `evidence.canceled.cancellation_reason` | string or "" (to unset) |  |  |
| `evidence.canceled.expected_at` | timestamp (Unix seconds) or "" (to unset) |  |  |
| `evidence.canceled.explanation` | string or "" (to unset) |  |  |
| `evidence.canceled.product_description` | string or "" (to unset) |  |  |
| `evidence.canceled.product_type` | enum: ``, `merchandise`, `service` |  |  |
| `evidence.canceled.return_status` | enum: ``, `merchant_rejected`, `successful` |  |  |
| `evidence.canceled.returned_at` | timestamp (Unix seconds) or "" (to unset) |  |  |
| `evidence.duplicate` | object or "" (to unset) |  |  |
| `evidence.duplicate.additional_documentation` | string or "" (to unset) |  |  |
| `evidence.duplicate.card_statement` | string or "" (to unset) |  |  |
| `evidence.duplicate.cash_receipt` | string or "" (to unset) |  |  |
| `evidence.duplicate.check_image` | string or "" (to unset) |  |  |
| `evidence.duplicate.explanation` | string or "" (to unset) |  |  |
| `evidence.duplicate.original_transaction` | string |  |  |
| `evidence.fraudulent` | object or "" (to unset) |  |  |
| `evidence.fraudulent.additional_documentation` | string or "" (to unset) |  |  |
| `evidence.fraudulent.explanation` | string or "" (to unset) |  |  |
| `evidence.merchandise_not_as_described` | object or "" (to unset) |  |  |
| `evidence.merchandise_not_as_described.additional_documentation` | string or "" (to unset) |  |  |
| `evidence.merchandise_not_as_described.explanation` | string or "" (to unset) |  |  |
| `evidence.merchandise_not_as_described.received_at` | timestamp (Unix seconds) or "" (to unset) |  |  |
| `evidence.merchandise_not_as_described.return_description` | string or "" (to unset) |  |  |
| `evidence.merchandise_not_as_described.return_status` | enum: ``, `merchant_rejected`, `successful` |  |  |
| `evidence.merchandise_not_as_described.returned_at` | timestamp (Unix seconds) or "" (to unset) |  |  |
| `evidence.not_received` | object or "" (to unset) |  |  |
| `evidence.not_received.additional_documentation` | string or "" (to unset) |  |  |
| `evidence.not_received.expected_at` | timestamp (Unix seconds) or "" (to unset) |  |  |
| `evidence.not_received.explanation` | string or "" (to unset) |  |  |
| `evidence.not_received.product_description` | string or "" (to unset) |  |  |
| `evidence.not_received.product_type` | enum: ``, `merchandise`, `service` |  |  |
| `evidence.other` | object or "" (to unset) |  |  |
| `evidence.other.additional_documentation` | string or "" (to unset) |  |  |
| `evidence.other.explanation` | string or "" (to unset) |  |  |
| `evidence.other.product_description` | string or "" (to unset) |  |  |
| `evidence.other.product_type` | enum: ``, `merchandise`, `service` |  |  |
| `evidence.reason` | enum: `canceled`, `duplicate`, `fraudulent`, `merchandise_not_as_described`, `not_received`, `other`, `service_not_as_described` |  |  |
| `evidence.service_not_as_described` | object or "" (to unset) |  |  |
| `evidence.service_not_as_described.additional_documentation` | string or "" (to unset) |  |  |
| `evidence.service_not_as_described.canceled_at` | timestamp (Unix seconds) or "" (to unset) |  |  |
| `evidence.service_not_as_described.cancellation_reason` | string or "" (to unset) |  |  |
| `evidence.service_not_as_described.explanation` | string or "" (to unset) |  |  |
| `evidence.service_not_as_described.received_at` | timestamp (Unix seconds) or "" (to unset) |  |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `transaction` | string |  | The ID of the issuing transaction to create a dispute for. For transaction on Treasury FinancialAccounts, use `treasury.received_debit`. |
| `treasury` | object |  | Params for disputes related to Treasury FinancialAccounts |
| `treasury.received_debit` | string | yes |  |

Returns: `issuing.dispute`

## GET /v1/issuing/disputes/{dispute}

operationId: `GetIssuingDisputesDispute`

Retrieves an Issuing `Dispute` object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `dispute (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `issuing.dispute`

## POST /v1/issuing/disputes/{dispute}

operationId: `PostIssuingDisputesDispute`

Updates the specified Issuing `Dispute` object by setting the values of the parameters passed. Any parameters not provided will be left unchanged. Properties on the `evidence` object can be unset by passing in an empty string.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `dispute (path)` | string | yes |  |
| `amount` | integer |  | The dispute amount in the card's currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). |
| `evidence` | object |  | Evidence provided for the dispute. |
| `evidence.canceled` | object or "" (to unset) |  |  |
| `evidence.canceled.additional_documentation` | string or "" (to unset) |  |  |
| `evidence.canceled.canceled_at` | timestamp (Unix seconds) or "" (to unset) |  |  |
| `evidence.canceled.cancellation_policy_provided` | boolean or "" (to unset) |  |  |
| `evidence.canceled.cancellation_reason` | string or "" (to unset) |  |  |
| `evidence.canceled.expected_at` | timestamp (Unix seconds) or "" (to unset) |  |  |
| `evidence.canceled.explanation` | string or "" (to unset) |  |  |
| `evidence.canceled.product_description` | string or "" (to unset) |  |  |
| `evidence.canceled.product_type` | enum: ``, `merchandise`, `service` |  |  |
| `evidence.canceled.return_status` | enum: ``, `merchant_rejected`, `successful` |  |  |
| `evidence.canceled.returned_at` | timestamp (Unix seconds) or "" (to unset) |  |  |
| `evidence.duplicate` | object or "" (to unset) |  |  |
| `evidence.duplicate.additional_documentation` | string or "" (to unset) |  |  |
| `evidence.duplicate.card_statement` | string or "" (to unset) |  |  |
| `evidence.duplicate.cash_receipt` | string or "" (to unset) |  |  |
| `evidence.duplicate.check_image` | string or "" (to unset) |  |  |
| `evidence.duplicate.explanation` | string or "" (to unset) |  |  |
| `evidence.duplicate.original_transaction` | string |  |  |
| `evidence.fraudulent` | object or "" (to unset) |  |  |
| `evidence.fraudulent.additional_documentation` | string or "" (to unset) |  |  |
| `evidence.fraudulent.explanation` | string or "" (to unset) |  |  |
| `evidence.merchandise_not_as_described` | object or "" (to unset) |  |  |
| `evidence.merchandise_not_as_described.additional_documentation` | string or "" (to unset) |  |  |
| `evidence.merchandise_not_as_described.explanation` | string or "" (to unset) |  |  |
| `evidence.merchandise_not_as_described.received_at` | timestamp (Unix seconds) or "" (to unset) |  |  |
| `evidence.merchandise_not_as_described.return_description` | string or "" (to unset) |  |  |
| `evidence.merchandise_not_as_described.return_status` | enum: ``, `merchant_rejected`, `successful` |  |  |
| `evidence.merchandise_not_as_described.returned_at` | timestamp (Unix seconds) or "" (to unset) |  |  |
| `evidence.not_received` | object or "" (to unset) |  |  |
| `evidence.not_received.additional_documentation` | string or "" (to unset) |  |  |
| `evidence.not_received.expected_at` | timestamp (Unix seconds) or "" (to unset) |  |  |
| `evidence.not_received.explanation` | string or "" (to unset) |  |  |
| `evidence.not_received.product_description` | string or "" (to unset) |  |  |
| `evidence.not_received.product_type` | enum: ``, `merchandise`, `service` |  |  |
| `evidence.other` | object or "" (to unset) |  |  |
| `evidence.other.additional_documentation` | string or "" (to unset) |  |  |
| `evidence.other.explanation` | string or "" (to unset) |  |  |
| `evidence.other.product_description` | string or "" (to unset) |  |  |
| `evidence.other.product_type` | enum: ``, `merchandise`, `service` |  |  |
| `evidence.reason` | enum: `canceled`, `duplicate`, `fraudulent`, `merchandise_not_as_described`, `not_received`, `other`, `service_not_as_described` |  |  |
| `evidence.service_not_as_described` | object or "" (to unset) |  |  |
| `evidence.service_not_as_described.additional_documentation` | string or "" (to unset) |  |  |
| `evidence.service_not_as_described.canceled_at` | timestamp (Unix seconds) or "" (to unset) |  |  |
| `evidence.service_not_as_described.cancellation_reason` | string or "" (to unset) |  |  |
| `evidence.service_not_as_described.explanation` | string or "" (to unset) |  |  |
| `evidence.service_not_as_described.received_at` | timestamp (Unix seconds) or "" (to unset) |  |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |

Returns: `issuing.dispute`

## POST /v1/issuing/disputes/{dispute}/submit

operationId: `PostIssuingDisputesDisputeSubmit`

Submits an Issuing `Dispute` to the card network. Stripe validates that all evidence fields required for the dispute’s reason are present. For more details, see [Dispute reasons and evidence](https://stripe.com/docs/issuing/purchases/disputes#dispute-reasons-and-evidence).

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `dispute (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |

Returns: `issuing.dispute`

## GET /v1/issuing/personalization_designs

operationId: `GetIssuingPersonalizationDesigns`

Returns a list of personalization design objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `lookup_keys` | array of string |  | Only return personalization designs with the given lookup keys. |
| `preferences` | object |  | Only return personalization designs with the given preferences. |
| `preferences.is_default` | boolean |  |  |
| `preferences.is_platform_default` | boolean |  |  |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `status` | enum: `active`, `inactive`, `rejected`, `review` |  | Only return personalization designs with the given status. |

Returns: object

## POST /v1/issuing/personalization_designs

operationId: `PostIssuingPersonalizationDesigns`

Creates a personalization design object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `card_logo` | string |  | The file for the card logo, for use with physical bundles that support card logos. Must have a `purpose` value of `issuing_logo`. |
| `carrier_text` | object |  | Hash containing carrier text, for use with physical bundles that support carrier text. |
| `carrier_text.footer_body` | string or "" (to unset) |  |  |
| `carrier_text.footer_title` | string or "" (to unset) |  |  |
| `carrier_text.header_body` | string or "" (to unset) |  |  |
| `carrier_text.header_title` | string or "" (to unset) |  |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `lookup_key` | string |  | A lookup key used to retrieve personalization designs dynamically from a static string. This may be up to 200 characters. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `name` | string |  | Friendly display name. |
| `physical_bundle` | string | yes | The physical bundle object belonging to this personalization design. |
| `preferences` | object |  | Information on whether this personalization design is used to create cards when one is not specified. |
| `preferences.is_default` | boolean | yes |  |
| `transfer_lookup_key` | boolean |  | If set to true, will atomically remove the lookup key from the existing personalization design, and assign it to this personalization design. |

Returns: `issuing.personalization_design`

## GET /v1/issuing/personalization_designs/{personalization_design}

operationId: `GetIssuingPersonalizationDesignsPersonalizationDesign`

Retrieves a personalization design object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `personalization_design (path)` | string | yes |  |

Returns: `issuing.personalization_design`

## POST /v1/issuing/personalization_designs/{personalization_design}

operationId: `PostIssuingPersonalizationDesignsPersonalizationDesign`

Updates a card personalization object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `personalization_design (path)` | string | yes |  |
| `card_logo` | string or "" (to unset) |  | The file for the card logo, for use with physical bundles that support card logos. Must have a `purpose` value of `issuing_logo`. |
| `carrier_text` | object or "" (to unset) |  | Hash containing carrier text, for use with physical bundles that support carrier text. |
| `carrier_text.footer_body` | string or "" (to unset) |  |  |
| `carrier_text.footer_title` | string or "" (to unset) |  |  |
| `carrier_text.header_body` | string or "" (to unset) |  |  |
| `carrier_text.header_title` | string or "" (to unset) |  |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `lookup_key` | string or "" (to unset) |  | A lookup key used to retrieve personalization designs dynamically from a static string. This may be up to 200 characters. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |
| `name` | string or "" (to unset) |  | Friendly display name. Providing an empty string will set the field to null. |
| `physical_bundle` | string |  | The physical bundle object belonging to this personalization design. |
| `preferences` | object |  | Information on whether this personalization design is used to create cards when one is not specified. |
| `preferences.is_default` | boolean | yes |  |
| `transfer_lookup_key` | boolean |  | If set to true, will atomically remove the lookup key from the existing personalization design, and assign it to this personalization design. |

Returns: `issuing.personalization_design`

## GET /v1/issuing/physical_bundles

operationId: `GetIssuingPhysicalBundles`

Returns a list of physical bundle objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `status` | enum: `active`, `inactive`, `review` |  | Only return physical bundles with the given status. |
| `type` | enum: `custom`, `standard` |  | Only return physical bundles with the given type. |

Returns: object

## GET /v1/issuing/physical_bundles/{physical_bundle}

operationId: `GetIssuingPhysicalBundlesPhysicalBundle`

Retrieves a physical bundle object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `physical_bundle (path)` | string | yes |  |

Returns: `issuing.physical_bundle`

## GET /v1/issuing/settlements

operationId: `GetIssuingSettlements`

Returns a list of Issuing `Settlement` objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | object or integer |  | Only return issuing settlements that were created during the given date interval. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## GET /v1/issuing/settlements/{settlement}

operationId: `GetIssuingSettlementsSettlement`

Retrieves an Issuing `Settlement` object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `settlement (path)` | string | yes |  |

Returns: `issuing.settlement`

## POST /v1/issuing/settlements/{settlement}

operationId: `PostIssuingSettlementsSettlement`

Updates the specified Issuing `Settlement` object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `settlement (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |

Returns: `issuing.settlement`

## GET /v1/issuing/tokens

operationId: `GetIssuingTokens`

Lists all Issuing `Token` objects for a given card.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `card` | string | yes | The Issuing card identifier to list tokens for. |
| `created` | object or integer |  | Only return Issuing tokens that were created during the given date interval. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `status` | enum: `active`, `deleted`, `requested`, `suspended` |  | Select Issuing tokens with the given status. |

Returns: object

## GET /v1/issuing/tokens/{token}

operationId: `GetIssuingTokensToken`

Retrieves an Issuing `Token` object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `token (path)` | string | yes |  |

Returns: `issuing.token`

## POST /v1/issuing/tokens/{token}

operationId: `PostIssuingTokensToken`

Attempts to update the specified Issuing `Token` object to the status specified.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `token (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `status` | enum: `active`, `deleted`, `suspended` | yes | Specifies which status the token should be updated to. |

Returns: `issuing.token`

## GET /v1/issuing/transactions

operationId: `GetIssuingTransactions`

Returns a list of Issuing `Transaction` objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `card` | string |  | Only return transactions that belong to the given card. |
| `cardholder` | string |  | Only return transactions that belong to the given cardholder. |
| `created` | object or integer |  | Only return transactions that were created during the given date interval. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |
| `type` | enum: `capture`, `refund` |  | Only return transactions that have the given type. One of `capture` or `refund`. |

Returns: object

## GET /v1/issuing/transactions/{transaction}

operationId: `GetIssuingTransactionsTransaction`

Retrieves an Issuing `Transaction` object.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `transaction (path)` | string | yes |  |

Returns: `issuing.transaction`

## POST /v1/issuing/transactions/{transaction}

operationId: `PostIssuingTransactionsTransaction`

Updates the specified Issuing `Transaction` object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `transaction (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `metadata` | map (key → value) or "" (to unset) |  | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. |

Returns: `issuing.transaction`

# Objects returned

## The `issuing.authorization` object

When an [issued card](https://stripe.com/docs/issuing) is used to make a purchase, an Issuing `Authorization`
object is created. [Authorizations](https://stripe.com/docs/issuing/purchases/authorizations) must be approved for the
purchase to be completed successfully.

Related guide: [Issued card authorizations](https://stripe.com/docs/issuing/purchases/authorizations)

Expandable fields (pass `expand[]=<field>`): `amount_details`, `balance_transactions`, `card`, `cardholder`, `merchant_data`, `network_data`, `pending_request`, `request_history`, `token`, `transactions`, `treasury`, `verification_data`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | The total amount that was authorized or rejected. This amount is in `currency` and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). `amount` should be the same as `merchant_amount`, unless `currency` and `merchant_currency` are different. |
| `amount_details` | `issuing_authorization_amount_details` |  | Detailed breakdown of amount components. These amounts are denominated in `currency` and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). |
| `approved` | boolean | yes | Whether the authorization has been approved. |
| `authorization_method` | enum: `chip`, `contactless`, `keyed_in`, `online`, `swipe` | yes | How the card details were provided. |
| `balance_transactions` | array of `balance_transaction` | yes | List of balance transactions associated with this authorization. |
| `card` | `issuing.card` | yes |  |
| `cardholder` | string or `issuing.cardholder` |  | The cardholder to whom this authorization belongs. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string | yes | The currency of the cardholder. This currency can be different from the currency presented at authorization and the `merchant_currency` field on this authorization. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `merchant_amount` | integer | yes | The total amount that was authorized or rejected. This amount is in the `merchant_currency` and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). `merchant_amount` should be the same as `amount`, unless `merchant_currency` and `currency` are different. |
| `merchant_currency` | string | yes | The local currency that was presented to the cardholder for the authorization. This currency can be different from the cardholder currency and the `currency` field on this authorization. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `merchant_data` | `issuing_authorization_merchant_data` | yes |  |
| `metadata` | map (key → value) | yes | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `network_data` | `issuing_authorization_network_data` |  | Details about the authorization, such as identifiers, set by the card network. |
| `object` | enum: `issuing.authorization` | yes | String representing the object's type. Objects of the same type share the same value. |
| `pending_request` | `issuing_authorization_pending_request` |  | The pending authorization request. This field will only be non-null during an `issuing_authorization.request` webhook. |
| `request_history` | array of `issuing_authorization_request` | yes | History of every time a `pending_request` authorization was approved/declined, either by you directly or by Stripe (e.g. based on your spending_controls). If the merchant changes the authorization by performing an incremental authorization, you can look at this field to see the previous requests for the authorization. This field can be helpful in determining why a given authorization was approved/declined. |
| `status` | enum: `closed`, `pending`, `reversed` | yes | The current status of the authorization in its lifecycle. |
| `token` | string or `issuing.token` |  | [Token](https://stripe.com/docs/api/issuing/tokens/object) object used for this authorization. If a network token was not used for this authorization, this field will be null. |
| `transactions` | array of `issuing.transaction` | yes | List of [transactions](https://stripe.com/docs/api/issuing/transactions) associated with this authorization. |
| `treasury` | `issuing_authorization_treasury` |  | [Treasury](https://stripe.com/docs/api/treasury) details related to this authorization if it was created on a [FinancialAccount](https://stripe.com/docs/api/treasury/financial_accounts). |
| `verification_data` | `issuing_authorization_verification_data` | yes |  |
| `wallet` | string |  | The digital wallet used for this transaction. One of `apple_pay`, `google_pay`, or `samsung_pay`. Will populate as `null` when no digital wallet was utilized. |

## The `issuing.cardholder` object

An Issuing `Cardholder` object represents an individual or business entity who is [issued](https://stripe.com/docs/issuing) cards.

Related guide: [How to create a cardholder](https://stripe.com/docs/issuing/cards#create-cardholder)

Expandable fields (pass `expand[]=<field>`): `billing`, `company`, `individual`, `requirements`, `spending_controls`

| Field | Type | Required | Description |
|---|---|---|---|
| `billing` | `issuing_cardholder_address` | yes |  |
| `company` | `issuing_cardholder_company` |  | Additional information about a `company` cardholder. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `email` | string |  | The cardholder's email address. |
| `id` | string | yes | Unique identifier for the object. |
| `individual` | `issuing_cardholder_individual` |  | Additional information about an `individual` cardholder. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metadata` | map (key → value) | yes | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `name` | string | yes | The cardholder's name. This will be printed on cards issued to them. |
| `object` | enum: `issuing.cardholder` | yes | String representing the object's type. Objects of the same type share the same value. |
| `phone_number` | string |  | The cardholder's phone number. This is required for all cardholders who will be creating EU cards. See the [3D Secure documentation](https://stripe.com/docs/issuing/3d-secure#when-is-3d-secure-applied) for more details. |
| `preferred_locales` | array of enum: `de`, `en`, `es`, `fr`, `it` |  | The cardholder’s preferred locales (languages), ordered by preference. Locales can be `de`, `en`, `es`, `fr`, or `it`.  This changes the language of the [3D Secure flow](https://stripe.com/docs/issuing/3d-secure) and one-time password messages sent to the cardholder. |
| `requirements` | `issuing_cardholder_requirements` | yes |  |
| `spending_controls` | `issuing_cardholder_authorization_controls` |  | Rules that control spending across this cardholder's cards. Refer to our [documentation](https://stripe.com/docs/issuing/controls/spending-controls) for more details. |
| `status` | enum: `active`, `blocked`, `inactive` | yes | Specifies whether to permit authorizations on this cardholder's cards. |
| `type` | enum: `company`, `individual` | yes | One of `individual` or `company`. See [Choose a cardholder type](https://stripe.com/docs/issuing/other/choose-cardholder) for more details. |

## The `issuing.card` object

You can [create physical or virtual cards](https://stripe.com/docs/issuing/cards) that are issued to cardholders.

Expandable fields (pass `expand[]=<field>`): `cardholder`, `personalization_design`, `replaced_by`, `replacement_for`, `shipping`, `spending_controls`, `wallets`

| Field | Type | Required | Description |
|---|---|---|---|
| `brand` | string | yes | The brand of the card. |
| `cancellation_reason` | enum: `design_rejected`, `lost`, `stolen` |  | The reason why the card was canceled. |
| `cardholder` | `issuing.cardholder` | yes |  |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Supported currencies are `usd` in the US, `eur` in the EU, and `gbp` in the UK. |
| `cvc` | string |  | The card's CVC. For security reasons, this is only available for virtual cards, and will be omitted unless you explicitly request it with [the `expand` parameter](https://stripe.com/docs/api/expanding_objects). Additionally, it's only available via the ["Retrieve a card" endpoint](https://stripe.com/docs/api/issuing/cards/retrieve), not via "List all cards" or any other endpoint. |
| `exp_month` | integer | yes | The expiration month of the card. |
| `exp_year` | integer | yes | The expiration year of the card. |
| `financial_account` | string |  | The financial account this card is attached to. |
| `id` | string | yes | Unique identifier for the object. |
| `last4` | string | yes | The last 4 digits of the card number. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metadata` | map (key → value) | yes | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `number` | string |  | The full unredacted card number. For security reasons, this is only available for virtual cards, and will be omitted unless you explicitly request it with [the `expand` parameter](https://stripe.com/docs/api/expanding_objects). Additionally, it's only available via the ["Retrieve a card" endpoint](https://stripe.com/docs/api/issuing/cards/retrieve), not via "List all cards" or any other endpoint. |
| `object` | enum: `issuing.card` | yes | String representing the object's type. Objects of the same type share the same value. |
| `personalization_design` | string or `issuing.personalization_design` |  | The personalization design object belonging to this card. |
| `replaced_by` | string or `issuing.card` |  | The latest card that replaces this card, if any. |
| `replacement_for` | string or `issuing.card` |  | The card this card replaces, if any. |
| `replacement_reason` | enum: `damaged`, `expired`, `lost`, `stolen` |  | The reason why the previous card needed to be replaced. |
| `shipping` | `issuing_card_shipping` |  | Where and how the card will be shipped. |
| `spending_controls` | `issuing_card_authorization_controls` | yes |  |
| `status` | enum: `active`, `canceled`, `inactive` | yes | Whether authorizations can be approved on this card. May be blocked from activating cards depending on past-due Cardholder requirements. Defaults to `inactive`. |
| `type` | enum: `physical`, `virtual` | yes | The type of the card. |
| `wallets` | `issuing_card_wallets` |  | Information relating to digital wallets (like Apple Pay and Google Pay). |

## The `issuing.dispute` object

As a [card issuer](https://stripe.com/docs/issuing), you can dispute transactions that the cardholder does not recognize, suspects to be fraudulent, or has other issues with.

Related guide: [Issuing disputes](https://stripe.com/docs/issuing/purchases/disputes)

Expandable fields (pass `expand[]=<field>`): `balance_transactions`, `evidence`, `transaction`, `treasury`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | Disputed amount in the card's currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). Usually the amount of the `transaction`, but can differ (usually because of currency fluctuation). |
| `balance_transactions` | array of `balance_transaction` |  | List of balance transactions associated with the dispute. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string | yes | The currency the `transaction` was made in. |
| `evidence` | `issuing_dispute_evidence` | yes |  |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metadata` | map (key → value) | yes | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `object` | enum: `issuing.dispute` | yes | String representing the object's type. Objects of the same type share the same value. |
| `status` | enum: `expired`, `lost`, `submitted`, `unsubmitted`, `won` | yes | Current status of the dispute. |
| `transaction` | string or `issuing.transaction` | yes | The transaction being disputed. |
| `treasury` | `issuing_dispute_treasury` |  | [Treasury](https://stripe.com/docs/api/treasury) details related to this dispute if it was created on a [FinancialAccount](/docs/api/treasury/financial_accounts |

## The `issuing.personalization_design` object

A Personalization Design is a logical grouping of a Physical Bundle, card logo, and carrier text that represents a product line.

Expandable fields (pass `expand[]=<field>`): `card_logo`, `carrier_text`, `physical_bundle`, `preferences`, `rejection_reasons`

| Field | Type | Required | Description |
|---|---|---|---|
| `card_logo` | string or `file` |  | The file for the card logo to use with physical bundles that support card logos. Must have a `purpose` value of `issuing_logo`. |
| `carrier_text` | `issuing_personalization_design_carrier_text` |  | Hash containing carrier text, for use with physical bundles that support carrier text. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `lookup_key` | string |  | A lookup key used to retrieve personalization designs dynamically from a static string. This may be up to 200 characters. |
| `metadata` | map (key → value) | yes | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `name` | string |  | Friendly display name. |
| `object` | enum: `issuing.personalization_design` | yes | String representing the object's type. Objects of the same type share the same value. |
| `physical_bundle` | string or `issuing.physical_bundle` | yes | The physical bundle object belonging to this personalization design. |
| `preferences` | `issuing_personalization_design_preferences` | yes |  |
| `rejection_reasons` | `issuing_personalization_design_rejection_reasons` | yes |  |
| `status` | enum: `active`, `inactive`, `rejected`, `review` | yes | Whether this personalization design can be used to create cards. |

## The `issuing.physical_bundle` object

A Physical Bundle represents the bundle of physical items - card stock, carrier letter, and envelope - that is shipped to a cardholder when you create a physical card.

Expandable fields (pass `expand[]=<field>`): `features`

| Field | Type | Required | Description |
|---|---|---|---|
| `features` | `issuing_physical_bundle_features` |  |  |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `name` | string | yes | Friendly display name. |
| `object` | enum: `issuing.physical_bundle` | yes | String representing the object's type. Objects of the same type share the same value. |
| `status` | enum: `active`, `inactive`, `review` | yes | Whether this physical bundle can be used to create cards. |
| `type` | enum: `custom`, `standard` | yes | Whether this physical bundle is a standard Stripe offering or custom-made for you. |

## The `issuing.settlement` object

When a non-stripe BIN is used, any use of an [issued card](https://stripe.com/docs/issuing) must be settled directly with the card network. The net amount owed is represented by an Issuing `Settlement` object.

| Field | Type | Required | Description |
|---|---|---|---|
| `bin` | string | yes | The Bank Identification Number reflecting this settlement record. |
| `clearing_date` | integer | yes | The date that the transactions are cleared and posted to user's accounts. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `id` | string | yes | Unique identifier for the object. |
| `interchange_fees` | integer | yes | The total interchange received as reimbursement for the transactions. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `metadata` | map (key → value) | yes | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `net_total` | integer | yes | The total net amount required to settle with the network. |
| `network` | enum: `visa` | yes | The card network for this settlement report. One of ["visa"] |
| `network_fees` | integer | yes | The total amount of fees owed to the network. |
| `network_settlement_identifier` | string | yes | The Settlement Identification Number assigned by the network. |
| `object` | enum: `issuing.settlement` | yes | String representing the object's type. Objects of the same type share the same value. |
| `settlement_service` | string | yes | One of `international` or `uk_national_net`. |
| `transaction_count` | integer | yes | The total number of transactions reflected in this settlement. |
| `transaction_volume` | integer | yes | The total transaction amount reflected in this settlement. |

## The `issuing.token` object

An issuing token object is created when an issued card is added to a digital wallet. As a [card issuer](https://stripe.com/docs/issuing), you can [view and manage these tokens](https://stripe.com/docs/issuing/controls/token-management) through Stripe.

Expandable fields (pass `expand[]=<field>`): `card`, `network_data`

| Field | Type | Required | Description |
|---|---|---|---|
| `card` | string or `issuing.card` | yes | Card associated with this token. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `device_fingerprint` | string |  | The hashed ID derived from the device ID from the card network associated with the token. |
| `id` | string | yes | Unique identifier for the object. |
| `last4` | string |  | The last four digits of the token. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `network` | enum: `mastercard`, `visa` | yes | The token service provider / card network associated with the token. |
| `network_data` | `issuing_network_token_network_data` |  |  |
| `network_updated_at` | timestamp (Unix seconds) | yes | Time at which the token was last updated by the card network. Measured in seconds since the Unix epoch. |
| `object` | enum: `issuing.token` | yes | String representing the object's type. Objects of the same type share the same value. |
| `status` | enum: `active`, `deleted`, `requested`, `suspended` | yes | The usage state of the token. |
| `wallet_provider` | enum: `apple_pay`, `google_pay`, `samsung_pay` |  | The digital wallet for this token, if one was used. |

## The `issuing.transaction` object

Any use of an [issued card](https://stripe.com/docs/issuing) that results in funds entering or leaving
your Stripe account, such as a completed purchase or refund, is represented by an Issuing
`Transaction` object.

Related guide: [Issued card transactions](https://stripe.com/docs/issuing/purchases/transactions)

Expandable fields (pass `expand[]=<field>`): `amount_details`, `authorization`, `balance_transaction`, `card`, `cardholder`, `dispute`, `merchant_data`, `network_data`, `purchase_details`, `token`, `treasury`

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | The transaction amount, which will be reflected in your balance. This amount is in your currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). |
| `amount_details` | `issuing_transaction_amount_details` |  | Detailed breakdown of amount components. These amounts are denominated in `currency` and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). |
| `authorization` | string or `issuing.authorization` |  | The `Authorization` object that led to this transaction. |
| `balance_transaction` | string or `balance_transaction` |  | ID of the [balance transaction](https://stripe.com/docs/api/balance_transactions) associated with this transaction. |
| `card` | string or `issuing.card` | yes | The card used to make this transaction. |
| `cardholder` | string or `issuing.cardholder` |  | The cardholder to whom this transaction belongs. |
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `currency` | string | yes | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `dispute` | string or `issuing.dispute` |  | If you've disputed the transaction, the ID of the dispute. |
| `id` | string | yes | Unique identifier for the object. |
| `livemode` | boolean | yes | Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode. |
| `merchant_amount` | integer | yes | The amount that the merchant will receive, denominated in `merchant_currency` and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). It will be different from `amount` if the merchant is taking payment in a different currency. |
| `merchant_currency` | string | yes | The currency with which the merchant is taking payment. |
| `merchant_data` | `issuing_authorization_merchant_data` | yes |  |
| `metadata` | map (key → value) | yes | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. |
| `network_data` | `issuing_transaction_network_data` |  | Details about the transaction, such as processing dates, set by the card network. |
| `object` | enum: `issuing.transaction` | yes | String representing the object's type. Objects of the same type share the same value. |
| `purchase_details` | `issuing_transaction_purchase_details` |  | Additional purchase information that is optionally provided by the merchant. |
| `token` | string or `issuing.token` |  | [Token](https://stripe.com/docs/api/issuing/tokens/object) object used for this transaction. If a network token was not used for this transaction, this field will be null. |
| `treasury` | `issuing_transaction_treasury` |  | [Treasury](https://stripe.com/docs/api/treasury) details related to this transaction if it was created on a [FinancialAccount](/docs/api/treasury/financial_accounts |
| `type` | enum: `capture`, `refund` | yes | The nature of the transaction. |
| `wallet` | enum: `apple_pay`, `google_pay`, `samsung_pay` |  | The digital wallet used for this transaction. One of `apple_pay`, `google_pay`, or `samsung_pay`. |

