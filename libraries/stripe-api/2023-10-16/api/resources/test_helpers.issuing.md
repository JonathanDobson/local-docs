# Stripe API 2023-10-16 — test helpers / issuing

Operations under `/v1/test_helpers/issuing` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## POST /v1/test_helpers/issuing/authorizations

operationId: `PostTestHelpersIssuingAuthorizations`

Create a test-mode authorization.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | The total amount to attempt to authorize. This amount is in the provided currency, or defaults to the card's currency, and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). |
| `amount_details` | object |  | Detailed breakdown of amount components. These amounts are denominated in `currency` and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). |
| `amount_details.atm_fee` | integer |  |  |
| `amount_details.cashback_amount` | integer |  |  |
| `authorization_method` | enum: `chip`, `contactless`, `keyed_in`, `online`, `swipe` |  | How the card details were provided. Defaults to online. |
| `card` | string | yes | Card associated with this authorization. |
| `currency` | string |  | The currency of the authorization. If not provided, defaults to the currency of the card. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `is_amount_controllable` | boolean |  | If set `true`, you may provide [amount](https://stripe.com/docs/api/issuing/authorizations/approve#approve_issuing_authorization-amount) to control how much to hold for the authorization. |
| `merchant_data` | object |  | Details about the seller (grocery store, e-commerce website, etc.) where the card authorization happened. |
| `merchant_data.category` | enum: `ac_refrigeration_repair`, `accounting_bookkeeping_services`, `advertising_services`, `agricultural_cooperative`, `airlines_air_carriers`, `airports_flying_fields`, `ambulance_services`, `amusement_parks_carnivals`, `antique_reproductions`, `antique_shops`, `aquariums`, `architectural_surveying_services`, `art_dealers_and_galleries`, `artists_supply_and_craft_shops`, `auto_and_home_supply_stores`, `auto_body_repair_shops`, `auto_paint_shops`, `auto_service_shops`, `automated_cash_disburse`, `automated_fuel_dispensers`, `automobile_associations`, `automotive_parts_and_accessories_stores`, `automotive_tire_stores`, `bail_and_bond_payments`, `bakeries`, `bands_orchestras`, `barber_and_beauty_shops`, `betting_casino_gambling`, `bicycle_shops`, `billiard_pool_establishments`, `boat_dealers`, `boat_rentals_and_leases`, `book_stores`, `books_periodicals_and_newspapers`, `bowling_alleys`, `bus_lines`, `business_secretarial_schools`, `buying_shopping_services`, `cable_satellite_and_other_pay_television_and_radio`, `camera_and_photographic_supply_stores`, `candy_nut_and_confectionery_stores`, `car_and_truck_dealers_new_used`, `car_and_truck_dealers_used_only`, `car_rental_agencies`, `car_washes`, `carpentry_services`, `carpet_upholstery_cleaning`, `caterers`, `charitable_and_social_service_organizations_fundraising`, `chemicals_and_allied_products`, `child_care_services`, `childrens_and_infants_wear_stores`, `chiropodists_podiatrists`, `chiropractors`, `cigar_stores_and_stands`, `civic_social_fraternal_associations`, `cleaning_and_maintenance`, `clothing_rental`, `colleges_universities`, `commercial_equipment`, `commercial_footwear`, `commercial_photography_art_and_graphics`, `commuter_transport_and_ferries`, `computer_network_services`, `computer_programming`, `computer_repair`, `computer_software_stores`, `computers_peripherals_and_software`, `concrete_work_services`, `construction_materials`, `consulting_public_relations`, `correspondence_schools`, `cosmetic_stores`, `counseling_services`, `country_clubs`, `courier_services`, `court_costs`, `credit_reporting_agencies`, `cruise_lines`, `dairy_products_stores`, `dance_hall_studios_schools`, `dating_escort_services`, `dentists_orthodontists`, `department_stores`, `detective_agencies`, `digital_goods_applications`, `digital_goods_games`, `digital_goods_large_volume`, `digital_goods_media`, `direct_marketing_catalog_merchant`, `direct_marketing_combination_catalog_and_retail_merchant`, `direct_marketing_inbound_telemarketing`, `direct_marketing_insurance_services`, `direct_marketing_other`, `direct_marketing_outbound_telemarketing`, `direct_marketing_subscription`, `direct_marketing_travel`, `discount_stores`, `doctors`, `door_to_door_sales`, `drapery_window_covering_and_upholstery_stores`, `drinking_places`, `drug_stores_and_pharmacies`, `drugs_drug_proprietaries_and_druggist_sundries`, `dry_cleaners`, `durable_goods`, `duty_free_stores`, `eating_places_restaurants`, `educational_services`, `electric_razor_stores`, `electric_vehicle_charging`, `electrical_parts_and_equipment`, `electrical_services`, `electronics_repair_shops`, `electronics_stores`, `elementary_secondary_schools`, `emergency_services_gcas_visa_use_only`, `employment_temp_agencies`, `equipment_rental`, `exterminating_services`, `family_clothing_stores`, `fast_food_restaurants`, `financial_institutions`, `fines_government_administrative_entities`, `fireplace_fireplace_screens_and_accessories_stores`, `floor_covering_stores`, `florists`, `florists_supplies_nursery_stock_and_flowers`, `freezer_and_locker_meat_provisioners`, `fuel_dealers_non_automotive`, `funeral_services_crematories`, `furniture_home_furnishings_and_equipment_stores_except_appliances`, `furniture_repair_refinishing`, `furriers_and_fur_shops`, `general_services`, `gift_card_novelty_and_souvenir_shops`, `glass_paint_and_wallpaper_stores`, `glassware_crystal_stores`, `golf_courses_public`, `government_licensed_horse_dog_racing_us_region_only`, `government_licensed_online_casions_online_gambling_us_region_only`, `government_owned_lotteries_non_us_region`, `government_owned_lotteries_us_region_only`, `government_services`, `grocery_stores_supermarkets`, `hardware_equipment_and_supplies`, `hardware_stores`, `health_and_beauty_spas`, `hearing_aids_sales_and_supplies`, `heating_plumbing_a_c`, `hobby_toy_and_game_shops`, `home_supply_warehouse_stores`, `hospitals`, `hotels_motels_and_resorts`, `household_appliance_stores`, `industrial_supplies`, `information_retrieval_services`, `insurance_default`, `insurance_underwriting_premiums`, `intra_company_purchases`, `jewelry_stores_watches_clocks_and_silverware_stores`, `landscaping_services`, `laundries`, `laundry_cleaning_services`, `legal_services_attorneys`, `luggage_and_leather_goods_stores`, `lumber_building_materials_stores`, `manual_cash_disburse`, `marinas_service_and_supplies`, `marketplaces`, `masonry_stonework_and_plaster`, `massage_parlors`, `medical_and_dental_labs`, `medical_dental_ophthalmic_and_hospital_equipment_and_supplies`, `medical_services`, `membership_organizations`, `mens_and_boys_clothing_and_accessories_stores`, `mens_womens_clothing_stores`, `metal_service_centers`, `miscellaneous_apparel_and_accessory_shops`, `miscellaneous_auto_dealers`, `miscellaneous_business_services`, `miscellaneous_food_stores`, `miscellaneous_general_merchandise`, `miscellaneous_general_services`, `miscellaneous_home_furnishing_specialty_stores`, `miscellaneous_publishing_and_printing`, `miscellaneous_recreation_services`, `miscellaneous_repair_shops`, `miscellaneous_specialty_retail`, `mobile_home_dealers`, `motion_picture_theaters`, `motor_freight_carriers_and_trucking`, `motor_homes_dealers`, `motor_vehicle_supplies_and_new_parts`, `motorcycle_shops_and_dealers`, `motorcycle_shops_dealers`, `music_stores_musical_instruments_pianos_and_sheet_music`, `news_dealers_and_newsstands`, `non_fi_money_orders`, `non_fi_stored_value_card_purchase_load`, `nondurable_goods`, `nurseries_lawn_and_garden_supply_stores`, `nursing_personal_care`, `office_and_commercial_furniture`, `opticians_eyeglasses`, `optometrists_ophthalmologist`, `orthopedic_goods_prosthetic_devices`, `osteopaths`, `package_stores_beer_wine_and_liquor`, `paints_varnishes_and_supplies`, `parking_lots_garages`, `passenger_railways`, `pawn_shops`, `pet_shops_pet_food_and_supplies`, `petroleum_and_petroleum_products`, `photo_developing`, `photographic_photocopy_microfilm_equipment_and_supplies`, `photographic_studios`, `picture_video_production`, `piece_goods_notions_and_other_dry_goods`, `plumbing_heating_equipment_and_supplies`, `political_organizations`, `postal_services_government_only`, `precious_stones_and_metals_watches_and_jewelry`, `professional_services`, `public_warehousing_and_storage`, `quick_copy_repro_and_blueprint`, `railroads`, `real_estate_agents_and_managers_rentals`, `record_stores`, `recreational_vehicle_rentals`, `religious_goods_stores`, `religious_organizations`, `roofing_siding_sheet_metal`, `secretarial_support_services`, `security_brokers_dealers`, `service_stations`, `sewing_needlework_fabric_and_piece_goods_stores`, `shoe_repair_hat_cleaning`, `shoe_stores`, `small_appliance_repair`, `snowmobile_dealers`, `special_trade_services`, `specialty_cleaning`, `sporting_goods_stores`, `sporting_recreation_camps`, `sports_and_riding_apparel_stores`, `sports_clubs_fields`, `stamp_and_coin_stores`, `stationary_office_supplies_printing_and_writing_paper`, `stationery_stores_office_and_school_supply_stores`, `swimming_pools_sales`, `t_ui_travel_germany`, `tailors_alterations`, `tax_payments_government_agencies`, `tax_preparation_services`, `taxicabs_limousines`, `telecommunication_equipment_and_telephone_sales`, `telecommunication_services`, `telegraph_services`, `tent_and_awning_shops`, `testing_laboratories`, `theatrical_ticket_agencies`, `timeshares`, `tire_retreading_and_repair`, `tolls_bridge_fees`, `tourist_attractions_and_exhibits`, `towing_services`, `trailer_parks_campgrounds`, `transportation_services`, `travel_agencies_tour_operators`, `truck_stop_iteration`, `truck_utility_trailer_rentals`, `typesetting_plate_making_and_related_services`, `typewriter_stores`, `u_s_federal_government_agencies_or_departments`, `uniforms_commercial_clothing`, `used_merchandise_and_secondhand_stores`, `utilities`, `variety_stores`, `veterinary_services`, `video_amusement_game_supplies`, `video_game_arcades`, `video_tape_rental_stores`, `vocational_trade_schools`, `watch_jewelry_repair`, `welding_repair`, `wholesale_clubs`, `wig_and_toupee_stores`, `wires_money_orders`, `womens_accessory_and_specialty_shops`, `womens_ready_to_wear_stores`, `wrecking_and_salvage_yards` |  |  |
| `merchant_data.city` | string |  |  |
| `merchant_data.country` | string |  |  |
| `merchant_data.name` | string |  |  |
| `merchant_data.network_id` | string |  |  |
| `merchant_data.postal_code` | string |  |  |
| `merchant_data.state` | string |  |  |
| `merchant_data.terminal_id` | string |  |  |
| `merchant_data.url` | string |  |  |
| `network_data` | object |  | Details about the authorization, such as identifiers, set by the card network. |
| `network_data.acquiring_institution_id` | string |  |  |
| `verification_data` | object |  | Verifications that Stripe performed on information that the cardholder provided to the merchant. |
| `verification_data.address_line1_check` | enum: `match`, `mismatch`, `not_provided` |  |  |
| `verification_data.address_postal_code_check` | enum: `match`, `mismatch`, `not_provided` |  |  |
| `verification_data.authentication_exemption` | object |  |  |
| `verification_data.authentication_exemption.claimed_by` | enum: `acquirer`, `issuer` | yes |  |
| `verification_data.authentication_exemption.type` | enum: `low_value_transaction`, `transaction_risk_analysis`, `unknown` | yes |  |
| `verification_data.cvc_check` | enum: `match`, `mismatch`, `not_provided` |  |  |
| `verification_data.expiry_check` | enum: `match`, `mismatch`, `not_provided` |  |  |
| `verification_data.three_d_secure` | object |  |  |
| `verification_data.three_d_secure.result` | enum: `attempt_acknowledged`, `authenticated`, `failed`, `required` | yes |  |
| `wallet` | enum: `apple_pay`, `google_pay`, `samsung_pay` |  | The digital wallet used for this transaction. One of `apple_pay`, `google_pay`, or `samsung_pay`. Will populate as `null` when no digital wallet was utilized. |

Returns: `issuing.authorization`

## POST /v1/test_helpers/issuing/authorizations/{authorization}/capture

operationId: `PostTestHelpersIssuingAuthorizationsAuthorizationCapture`

Capture a test-mode authorization.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `authorization (path)` | string | yes |  |
| `capture_amount` | integer |  | The amount to capture from the authorization. If not provided, the full amount of the authorization will be captured. This amount is in the authorization currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). |
| `close_authorization` | boolean |  | Whether to close the authorization after capture. Defaults to true. Set to false to enable multi-capture flows. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `purchase_details` | object |  | Additional purchase information that is optionally provided by the merchant. |
| `purchase_details.flight` | object |  |  |
| `purchase_details.flight.departure_at` | timestamp (Unix seconds) |  |  |
| `purchase_details.flight.passenger_name` | string |  |  |
| `purchase_details.flight.refundable` | boolean |  |  |
| `purchase_details.flight.segments` | array of object |  |  |
| `purchase_details.flight.segments[].arrival_airport_code` | string |  |  |
| `purchase_details.flight.segments[].carrier` | string |  |  |
| `purchase_details.flight.segments[].departure_airport_code` | string |  |  |
| `purchase_details.flight.segments[].flight_number` | string |  |  |
| `purchase_details.flight.segments[].service_class` | string |  |  |
| `purchase_details.flight.segments[].stopover_allowed` | boolean |  |  |
| `purchase_details.flight.travel_agency` | string |  |  |
| `purchase_details.fuel` | object |  |  |
| `purchase_details.fuel.type` | enum: `diesel`, `other`, `unleaded_plus`, `unleaded_regular`, `unleaded_super` |  |  |
| `purchase_details.fuel.unit` | enum: `liter`, `us_gallon` |  |  |
| `purchase_details.fuel.unit_cost_decimal` | string |  |  |
| `purchase_details.fuel.volume_decimal` | string |  |  |
| `purchase_details.lodging` | object |  |  |
| `purchase_details.lodging.check_in_at` | timestamp (Unix seconds) |  |  |
| `purchase_details.lodging.nights` | integer |  |  |
| `purchase_details.receipt` | array of object |  |  |
| `purchase_details.receipt[].description` | string |  |  |
| `purchase_details.receipt[].quantity` | string |  |  |
| `purchase_details.receipt[].total` | integer |  |  |
| `purchase_details.receipt[].unit_cost` | integer |  |  |
| `purchase_details.reference` | string |  |  |

Returns: `issuing.authorization`

## POST /v1/test_helpers/issuing/authorizations/{authorization}/expire

operationId: `PostTestHelpersIssuingAuthorizationsAuthorizationExpire`

Expire a test-mode Authorization.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `authorization (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `issuing.authorization`

## POST /v1/test_helpers/issuing/authorizations/{authorization}/increment

operationId: `PostTestHelpersIssuingAuthorizationsAuthorizationIncrement`

Increment a test-mode Authorization.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `authorization (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `increment_amount` | integer | yes | The amount to increment the authorization by. This amount is in the authorization currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). |
| `is_amount_controllable` | boolean |  | If set `true`, you may provide [amount](https://stripe.com/docs/api/issuing/authorizations/approve#approve_issuing_authorization-amount) to control how much to hold for the authorization. |

Returns: `issuing.authorization`

## POST /v1/test_helpers/issuing/authorizations/{authorization}/reverse

operationId: `PostTestHelpersIssuingAuthorizationsAuthorizationReverse`

Reverse a test-mode Authorization.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `authorization (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `reverse_amount` | integer |  | The amount to reverse from the authorization. If not provided, the full amount of the authorization will be reversed. This amount is in the authorization currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). |

Returns: `issuing.authorization`

## POST /v1/test_helpers/issuing/cards/{card}/shipping/deliver

operationId: `PostTestHelpersIssuingCardsCardShippingDeliver`

Updates the shipping status of the specified Issuing `Card` object to `delivered`.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `card (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `issuing.card`

## POST /v1/test_helpers/issuing/cards/{card}/shipping/fail

operationId: `PostTestHelpersIssuingCardsCardShippingFail`

Updates the shipping status of the specified Issuing `Card` object to `failure`.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `card (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `issuing.card`

## POST /v1/test_helpers/issuing/cards/{card}/shipping/return

operationId: `PostTestHelpersIssuingCardsCardShippingReturn`

Updates the shipping status of the specified Issuing `Card` object to `returned`.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `card (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `issuing.card`

## POST /v1/test_helpers/issuing/cards/{card}/shipping/ship

operationId: `PostTestHelpersIssuingCardsCardShippingShip`

Updates the shipping status of the specified Issuing `Card` object to `shipped`.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `card (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `issuing.card`

## POST /v1/test_helpers/issuing/personalization_designs/{personalization_design}/activate

operationId: `PostTestHelpersIssuingPersonalizationDesignsPersonalizationDesignActivate`

Updates the `status` of the specified testmode personalization design object to `active`.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `personalization_design (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `issuing.personalization_design`

## POST /v1/test_helpers/issuing/personalization_designs/{personalization_design}/deactivate

operationId: `PostTestHelpersIssuingPersonalizationDesignsPersonalizationDesignDeactivate`

Updates the `status` of the specified testmode personalization design object to `inactive`.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `personalization_design (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |

Returns: `issuing.personalization_design`

## POST /v1/test_helpers/issuing/personalization_designs/{personalization_design}/reject

operationId: `PostTestHelpersIssuingPersonalizationDesignsPersonalizationDesignReject`

Updates the `status` of the specified testmode personalization design object to `rejected`.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `personalization_design (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `rejection_reasons` | object | yes | The reason(s) the personalization design was rejected. |
| `rejection_reasons.card_logo` | array of enum: `geographic_location`, `inappropriate`, `network_name`, `non_binary_image`, `non_fiat_currency`, `other`, `other_entity`, `promotional_material` |  |  |
| `rejection_reasons.carrier_text` | array of enum: `geographic_location`, `inappropriate`, `network_name`, `non_fiat_currency`, `other`, `other_entity`, `promotional_material` |  |  |

Returns: `issuing.personalization_design`

## POST /v1/test_helpers/issuing/transactions/create_force_capture

operationId: `PostTestHelpersIssuingTransactionsCreateForceCapture`

Allows the user to capture an arbitrary amount, also known as a forced capture.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | The total amount to attempt to capture. This amount is in the provided currency, or defaults to the cards currency, and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). |
| `card` | string | yes | Card associated with this transaction. |
| `currency` | string |  | The currency of the capture. If not provided, defaults to the currency of the card. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `merchant_data` | object |  | Details about the seller (grocery store, e-commerce website, etc.) where the card authorization happened. |
| `merchant_data.category` | enum: `ac_refrigeration_repair`, `accounting_bookkeeping_services`, `advertising_services`, `agricultural_cooperative`, `airlines_air_carriers`, `airports_flying_fields`, `ambulance_services`, `amusement_parks_carnivals`, `antique_reproductions`, `antique_shops`, `aquariums`, `architectural_surveying_services`, `art_dealers_and_galleries`, `artists_supply_and_craft_shops`, `auto_and_home_supply_stores`, `auto_body_repair_shops`, `auto_paint_shops`, `auto_service_shops`, `automated_cash_disburse`, `automated_fuel_dispensers`, `automobile_associations`, `automotive_parts_and_accessories_stores`, `automotive_tire_stores`, `bail_and_bond_payments`, `bakeries`, `bands_orchestras`, `barber_and_beauty_shops`, `betting_casino_gambling`, `bicycle_shops`, `billiard_pool_establishments`, `boat_dealers`, `boat_rentals_and_leases`, `book_stores`, `books_periodicals_and_newspapers`, `bowling_alleys`, `bus_lines`, `business_secretarial_schools`, `buying_shopping_services`, `cable_satellite_and_other_pay_television_and_radio`, `camera_and_photographic_supply_stores`, `candy_nut_and_confectionery_stores`, `car_and_truck_dealers_new_used`, `car_and_truck_dealers_used_only`, `car_rental_agencies`, `car_washes`, `carpentry_services`, `carpet_upholstery_cleaning`, `caterers`, `charitable_and_social_service_organizations_fundraising`, `chemicals_and_allied_products`, `child_care_services`, `childrens_and_infants_wear_stores`, `chiropodists_podiatrists`, `chiropractors`, `cigar_stores_and_stands`, `civic_social_fraternal_associations`, `cleaning_and_maintenance`, `clothing_rental`, `colleges_universities`, `commercial_equipment`, `commercial_footwear`, `commercial_photography_art_and_graphics`, `commuter_transport_and_ferries`, `computer_network_services`, `computer_programming`, `computer_repair`, `computer_software_stores`, `computers_peripherals_and_software`, `concrete_work_services`, `construction_materials`, `consulting_public_relations`, `correspondence_schools`, `cosmetic_stores`, `counseling_services`, `country_clubs`, `courier_services`, `court_costs`, `credit_reporting_agencies`, `cruise_lines`, `dairy_products_stores`, `dance_hall_studios_schools`, `dating_escort_services`, `dentists_orthodontists`, `department_stores`, `detective_agencies`, `digital_goods_applications`, `digital_goods_games`, `digital_goods_large_volume`, `digital_goods_media`, `direct_marketing_catalog_merchant`, `direct_marketing_combination_catalog_and_retail_merchant`, `direct_marketing_inbound_telemarketing`, `direct_marketing_insurance_services`, `direct_marketing_other`, `direct_marketing_outbound_telemarketing`, `direct_marketing_subscription`, `direct_marketing_travel`, `discount_stores`, `doctors`, `door_to_door_sales`, `drapery_window_covering_and_upholstery_stores`, `drinking_places`, `drug_stores_and_pharmacies`, `drugs_drug_proprietaries_and_druggist_sundries`, `dry_cleaners`, `durable_goods`, `duty_free_stores`, `eating_places_restaurants`, `educational_services`, `electric_razor_stores`, `electric_vehicle_charging`, `electrical_parts_and_equipment`, `electrical_services`, `electronics_repair_shops`, `electronics_stores`, `elementary_secondary_schools`, `emergency_services_gcas_visa_use_only`, `employment_temp_agencies`, `equipment_rental`, `exterminating_services`, `family_clothing_stores`, `fast_food_restaurants`, `financial_institutions`, `fines_government_administrative_entities`, `fireplace_fireplace_screens_and_accessories_stores`, `floor_covering_stores`, `florists`, `florists_supplies_nursery_stock_and_flowers`, `freezer_and_locker_meat_provisioners`, `fuel_dealers_non_automotive`, `funeral_services_crematories`, `furniture_home_furnishings_and_equipment_stores_except_appliances`, `furniture_repair_refinishing`, `furriers_and_fur_shops`, `general_services`, `gift_card_novelty_and_souvenir_shops`, `glass_paint_and_wallpaper_stores`, `glassware_crystal_stores`, `golf_courses_public`, `government_licensed_horse_dog_racing_us_region_only`, `government_licensed_online_casions_online_gambling_us_region_only`, `government_owned_lotteries_non_us_region`, `government_owned_lotteries_us_region_only`, `government_services`, `grocery_stores_supermarkets`, `hardware_equipment_and_supplies`, `hardware_stores`, `health_and_beauty_spas`, `hearing_aids_sales_and_supplies`, `heating_plumbing_a_c`, `hobby_toy_and_game_shops`, `home_supply_warehouse_stores`, `hospitals`, `hotels_motels_and_resorts`, `household_appliance_stores`, `industrial_supplies`, `information_retrieval_services`, `insurance_default`, `insurance_underwriting_premiums`, `intra_company_purchases`, `jewelry_stores_watches_clocks_and_silverware_stores`, `landscaping_services`, `laundries`, `laundry_cleaning_services`, `legal_services_attorneys`, `luggage_and_leather_goods_stores`, `lumber_building_materials_stores`, `manual_cash_disburse`, `marinas_service_and_supplies`, `marketplaces`, `masonry_stonework_and_plaster`, `massage_parlors`, `medical_and_dental_labs`, `medical_dental_ophthalmic_and_hospital_equipment_and_supplies`, `medical_services`, `membership_organizations`, `mens_and_boys_clothing_and_accessories_stores`, `mens_womens_clothing_stores`, `metal_service_centers`, `miscellaneous_apparel_and_accessory_shops`, `miscellaneous_auto_dealers`, `miscellaneous_business_services`, `miscellaneous_food_stores`, `miscellaneous_general_merchandise`, `miscellaneous_general_services`, `miscellaneous_home_furnishing_specialty_stores`, `miscellaneous_publishing_and_printing`, `miscellaneous_recreation_services`, `miscellaneous_repair_shops`, `miscellaneous_specialty_retail`, `mobile_home_dealers`, `motion_picture_theaters`, `motor_freight_carriers_and_trucking`, `motor_homes_dealers`, `motor_vehicle_supplies_and_new_parts`, `motorcycle_shops_and_dealers`, `motorcycle_shops_dealers`, `music_stores_musical_instruments_pianos_and_sheet_music`, `news_dealers_and_newsstands`, `non_fi_money_orders`, `non_fi_stored_value_card_purchase_load`, `nondurable_goods`, `nurseries_lawn_and_garden_supply_stores`, `nursing_personal_care`, `office_and_commercial_furniture`, `opticians_eyeglasses`, `optometrists_ophthalmologist`, `orthopedic_goods_prosthetic_devices`, `osteopaths`, `package_stores_beer_wine_and_liquor`, `paints_varnishes_and_supplies`, `parking_lots_garages`, `passenger_railways`, `pawn_shops`, `pet_shops_pet_food_and_supplies`, `petroleum_and_petroleum_products`, `photo_developing`, `photographic_photocopy_microfilm_equipment_and_supplies`, `photographic_studios`, `picture_video_production`, `piece_goods_notions_and_other_dry_goods`, `plumbing_heating_equipment_and_supplies`, `political_organizations`, `postal_services_government_only`, `precious_stones_and_metals_watches_and_jewelry`, `professional_services`, `public_warehousing_and_storage`, `quick_copy_repro_and_blueprint`, `railroads`, `real_estate_agents_and_managers_rentals`, `record_stores`, `recreational_vehicle_rentals`, `religious_goods_stores`, `religious_organizations`, `roofing_siding_sheet_metal`, `secretarial_support_services`, `security_brokers_dealers`, `service_stations`, `sewing_needlework_fabric_and_piece_goods_stores`, `shoe_repair_hat_cleaning`, `shoe_stores`, `small_appliance_repair`, `snowmobile_dealers`, `special_trade_services`, `specialty_cleaning`, `sporting_goods_stores`, `sporting_recreation_camps`, `sports_and_riding_apparel_stores`, `sports_clubs_fields`, `stamp_and_coin_stores`, `stationary_office_supplies_printing_and_writing_paper`, `stationery_stores_office_and_school_supply_stores`, `swimming_pools_sales`, `t_ui_travel_germany`, `tailors_alterations`, `tax_payments_government_agencies`, `tax_preparation_services`, `taxicabs_limousines`, `telecommunication_equipment_and_telephone_sales`, `telecommunication_services`, `telegraph_services`, `tent_and_awning_shops`, `testing_laboratories`, `theatrical_ticket_agencies`, `timeshares`, `tire_retreading_and_repair`, `tolls_bridge_fees`, `tourist_attractions_and_exhibits`, `towing_services`, `trailer_parks_campgrounds`, `transportation_services`, `travel_agencies_tour_operators`, `truck_stop_iteration`, `truck_utility_trailer_rentals`, `typesetting_plate_making_and_related_services`, `typewriter_stores`, `u_s_federal_government_agencies_or_departments`, `uniforms_commercial_clothing`, `used_merchandise_and_secondhand_stores`, `utilities`, `variety_stores`, `veterinary_services`, `video_amusement_game_supplies`, `video_game_arcades`, `video_tape_rental_stores`, `vocational_trade_schools`, `watch_jewelry_repair`, `welding_repair`, `wholesale_clubs`, `wig_and_toupee_stores`, `wires_money_orders`, `womens_accessory_and_specialty_shops`, `womens_ready_to_wear_stores`, `wrecking_and_salvage_yards` |  |  |
| `merchant_data.city` | string |  |  |
| `merchant_data.country` | string |  |  |
| `merchant_data.name` | string |  |  |
| `merchant_data.network_id` | string |  |  |
| `merchant_data.postal_code` | string |  |  |
| `merchant_data.state` | string |  |  |
| `merchant_data.terminal_id` | string |  |  |
| `merchant_data.url` | string |  |  |
| `purchase_details` | object |  | Additional purchase information that is optionally provided by the merchant. |
| `purchase_details.flight` | object |  |  |
| `purchase_details.flight.departure_at` | timestamp (Unix seconds) |  |  |
| `purchase_details.flight.passenger_name` | string |  |  |
| `purchase_details.flight.refundable` | boolean |  |  |
| `purchase_details.flight.segments` | array of object |  |  |
| `purchase_details.flight.segments[].arrival_airport_code` | string |  |  |
| `purchase_details.flight.segments[].carrier` | string |  |  |
| `purchase_details.flight.segments[].departure_airport_code` | string |  |  |
| `purchase_details.flight.segments[].flight_number` | string |  |  |
| `purchase_details.flight.segments[].service_class` | string |  |  |
| `purchase_details.flight.segments[].stopover_allowed` | boolean |  |  |
| `purchase_details.flight.travel_agency` | string |  |  |
| `purchase_details.fuel` | object |  |  |
| `purchase_details.fuel.type` | enum: `diesel`, `other`, `unleaded_plus`, `unleaded_regular`, `unleaded_super` |  |  |
| `purchase_details.fuel.unit` | enum: `liter`, `us_gallon` |  |  |
| `purchase_details.fuel.unit_cost_decimal` | string |  |  |
| `purchase_details.fuel.volume_decimal` | string |  |  |
| `purchase_details.lodging` | object |  |  |
| `purchase_details.lodging.check_in_at` | timestamp (Unix seconds) |  |  |
| `purchase_details.lodging.nights` | integer |  |  |
| `purchase_details.receipt` | array of object |  |  |
| `purchase_details.receipt[].description` | string |  |  |
| `purchase_details.receipt[].quantity` | string |  |  |
| `purchase_details.receipt[].total` | integer |  |  |
| `purchase_details.receipt[].unit_cost` | integer |  |  |
| `purchase_details.reference` | string |  |  |

Returns: `issuing.transaction`

## POST /v1/test_helpers/issuing/transactions/create_unlinked_refund

operationId: `PostTestHelpersIssuingTransactionsCreateUnlinkedRefund`

Allows the user to refund an arbitrary amount, also known as a unlinked refund.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | integer | yes | The total amount to attempt to refund. This amount is in the provided currency, or defaults to the cards currency, and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). |
| `card` | string | yes | Card associated with this unlinked refund transaction. |
| `currency` | string |  | The currency of the unlinked refund. If not provided, defaults to the currency of the card. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `merchant_data` | object |  | Details about the seller (grocery store, e-commerce website, etc.) where the card authorization happened. |
| `merchant_data.category` | enum: `ac_refrigeration_repair`, `accounting_bookkeeping_services`, `advertising_services`, `agricultural_cooperative`, `airlines_air_carriers`, `airports_flying_fields`, `ambulance_services`, `amusement_parks_carnivals`, `antique_reproductions`, `antique_shops`, `aquariums`, `architectural_surveying_services`, `art_dealers_and_galleries`, `artists_supply_and_craft_shops`, `auto_and_home_supply_stores`, `auto_body_repair_shops`, `auto_paint_shops`, `auto_service_shops`, `automated_cash_disburse`, `automated_fuel_dispensers`, `automobile_associations`, `automotive_parts_and_accessories_stores`, `automotive_tire_stores`, `bail_and_bond_payments`, `bakeries`, `bands_orchestras`, `barber_and_beauty_shops`, `betting_casino_gambling`, `bicycle_shops`, `billiard_pool_establishments`, `boat_dealers`, `boat_rentals_and_leases`, `book_stores`, `books_periodicals_and_newspapers`, `bowling_alleys`, `bus_lines`, `business_secretarial_schools`, `buying_shopping_services`, `cable_satellite_and_other_pay_television_and_radio`, `camera_and_photographic_supply_stores`, `candy_nut_and_confectionery_stores`, `car_and_truck_dealers_new_used`, `car_and_truck_dealers_used_only`, `car_rental_agencies`, `car_washes`, `carpentry_services`, `carpet_upholstery_cleaning`, `caterers`, `charitable_and_social_service_organizations_fundraising`, `chemicals_and_allied_products`, `child_care_services`, `childrens_and_infants_wear_stores`, `chiropodists_podiatrists`, `chiropractors`, `cigar_stores_and_stands`, `civic_social_fraternal_associations`, `cleaning_and_maintenance`, `clothing_rental`, `colleges_universities`, `commercial_equipment`, `commercial_footwear`, `commercial_photography_art_and_graphics`, `commuter_transport_and_ferries`, `computer_network_services`, `computer_programming`, `computer_repair`, `computer_software_stores`, `computers_peripherals_and_software`, `concrete_work_services`, `construction_materials`, `consulting_public_relations`, `correspondence_schools`, `cosmetic_stores`, `counseling_services`, `country_clubs`, `courier_services`, `court_costs`, `credit_reporting_agencies`, `cruise_lines`, `dairy_products_stores`, `dance_hall_studios_schools`, `dating_escort_services`, `dentists_orthodontists`, `department_stores`, `detective_agencies`, `digital_goods_applications`, `digital_goods_games`, `digital_goods_large_volume`, `digital_goods_media`, `direct_marketing_catalog_merchant`, `direct_marketing_combination_catalog_and_retail_merchant`, `direct_marketing_inbound_telemarketing`, `direct_marketing_insurance_services`, `direct_marketing_other`, `direct_marketing_outbound_telemarketing`, `direct_marketing_subscription`, `direct_marketing_travel`, `discount_stores`, `doctors`, `door_to_door_sales`, `drapery_window_covering_and_upholstery_stores`, `drinking_places`, `drug_stores_and_pharmacies`, `drugs_drug_proprietaries_and_druggist_sundries`, `dry_cleaners`, `durable_goods`, `duty_free_stores`, `eating_places_restaurants`, `educational_services`, `electric_razor_stores`, `electric_vehicle_charging`, `electrical_parts_and_equipment`, `electrical_services`, `electronics_repair_shops`, `electronics_stores`, `elementary_secondary_schools`, `emergency_services_gcas_visa_use_only`, `employment_temp_agencies`, `equipment_rental`, `exterminating_services`, `family_clothing_stores`, `fast_food_restaurants`, `financial_institutions`, `fines_government_administrative_entities`, `fireplace_fireplace_screens_and_accessories_stores`, `floor_covering_stores`, `florists`, `florists_supplies_nursery_stock_and_flowers`, `freezer_and_locker_meat_provisioners`, `fuel_dealers_non_automotive`, `funeral_services_crematories`, `furniture_home_furnishings_and_equipment_stores_except_appliances`, `furniture_repair_refinishing`, `furriers_and_fur_shops`, `general_services`, `gift_card_novelty_and_souvenir_shops`, `glass_paint_and_wallpaper_stores`, `glassware_crystal_stores`, `golf_courses_public`, `government_licensed_horse_dog_racing_us_region_only`, `government_licensed_online_casions_online_gambling_us_region_only`, `government_owned_lotteries_non_us_region`, `government_owned_lotteries_us_region_only`, `government_services`, `grocery_stores_supermarkets`, `hardware_equipment_and_supplies`, `hardware_stores`, `health_and_beauty_spas`, `hearing_aids_sales_and_supplies`, `heating_plumbing_a_c`, `hobby_toy_and_game_shops`, `home_supply_warehouse_stores`, `hospitals`, `hotels_motels_and_resorts`, `household_appliance_stores`, `industrial_supplies`, `information_retrieval_services`, `insurance_default`, `insurance_underwriting_premiums`, `intra_company_purchases`, `jewelry_stores_watches_clocks_and_silverware_stores`, `landscaping_services`, `laundries`, `laundry_cleaning_services`, `legal_services_attorneys`, `luggage_and_leather_goods_stores`, `lumber_building_materials_stores`, `manual_cash_disburse`, `marinas_service_and_supplies`, `marketplaces`, `masonry_stonework_and_plaster`, `massage_parlors`, `medical_and_dental_labs`, `medical_dental_ophthalmic_and_hospital_equipment_and_supplies`, `medical_services`, `membership_organizations`, `mens_and_boys_clothing_and_accessories_stores`, `mens_womens_clothing_stores`, `metal_service_centers`, `miscellaneous_apparel_and_accessory_shops`, `miscellaneous_auto_dealers`, `miscellaneous_business_services`, `miscellaneous_food_stores`, `miscellaneous_general_merchandise`, `miscellaneous_general_services`, `miscellaneous_home_furnishing_specialty_stores`, `miscellaneous_publishing_and_printing`, `miscellaneous_recreation_services`, `miscellaneous_repair_shops`, `miscellaneous_specialty_retail`, `mobile_home_dealers`, `motion_picture_theaters`, `motor_freight_carriers_and_trucking`, `motor_homes_dealers`, `motor_vehicle_supplies_and_new_parts`, `motorcycle_shops_and_dealers`, `motorcycle_shops_dealers`, `music_stores_musical_instruments_pianos_and_sheet_music`, `news_dealers_and_newsstands`, `non_fi_money_orders`, `non_fi_stored_value_card_purchase_load`, `nondurable_goods`, `nurseries_lawn_and_garden_supply_stores`, `nursing_personal_care`, `office_and_commercial_furniture`, `opticians_eyeglasses`, `optometrists_ophthalmologist`, `orthopedic_goods_prosthetic_devices`, `osteopaths`, `package_stores_beer_wine_and_liquor`, `paints_varnishes_and_supplies`, `parking_lots_garages`, `passenger_railways`, `pawn_shops`, `pet_shops_pet_food_and_supplies`, `petroleum_and_petroleum_products`, `photo_developing`, `photographic_photocopy_microfilm_equipment_and_supplies`, `photographic_studios`, `picture_video_production`, `piece_goods_notions_and_other_dry_goods`, `plumbing_heating_equipment_and_supplies`, `political_organizations`, `postal_services_government_only`, `precious_stones_and_metals_watches_and_jewelry`, `professional_services`, `public_warehousing_and_storage`, `quick_copy_repro_and_blueprint`, `railroads`, `real_estate_agents_and_managers_rentals`, `record_stores`, `recreational_vehicle_rentals`, `religious_goods_stores`, `religious_organizations`, `roofing_siding_sheet_metal`, `secretarial_support_services`, `security_brokers_dealers`, `service_stations`, `sewing_needlework_fabric_and_piece_goods_stores`, `shoe_repair_hat_cleaning`, `shoe_stores`, `small_appliance_repair`, `snowmobile_dealers`, `special_trade_services`, `specialty_cleaning`, `sporting_goods_stores`, `sporting_recreation_camps`, `sports_and_riding_apparel_stores`, `sports_clubs_fields`, `stamp_and_coin_stores`, `stationary_office_supplies_printing_and_writing_paper`, `stationery_stores_office_and_school_supply_stores`, `swimming_pools_sales`, `t_ui_travel_germany`, `tailors_alterations`, `tax_payments_government_agencies`, `tax_preparation_services`, `taxicabs_limousines`, `telecommunication_equipment_and_telephone_sales`, `telecommunication_services`, `telegraph_services`, `tent_and_awning_shops`, `testing_laboratories`, `theatrical_ticket_agencies`, `timeshares`, `tire_retreading_and_repair`, `tolls_bridge_fees`, `tourist_attractions_and_exhibits`, `towing_services`, `trailer_parks_campgrounds`, `transportation_services`, `travel_agencies_tour_operators`, `truck_stop_iteration`, `truck_utility_trailer_rentals`, `typesetting_plate_making_and_related_services`, `typewriter_stores`, `u_s_federal_government_agencies_or_departments`, `uniforms_commercial_clothing`, `used_merchandise_and_secondhand_stores`, `utilities`, `variety_stores`, `veterinary_services`, `video_amusement_game_supplies`, `video_game_arcades`, `video_tape_rental_stores`, `vocational_trade_schools`, `watch_jewelry_repair`, `welding_repair`, `wholesale_clubs`, `wig_and_toupee_stores`, `wires_money_orders`, `womens_accessory_and_specialty_shops`, `womens_ready_to_wear_stores`, `wrecking_and_salvage_yards` |  |  |
| `merchant_data.city` | string |  |  |
| `merchant_data.country` | string |  |  |
| `merchant_data.name` | string |  |  |
| `merchant_data.network_id` | string |  |  |
| `merchant_data.postal_code` | string |  |  |
| `merchant_data.state` | string |  |  |
| `merchant_data.terminal_id` | string |  |  |
| `merchant_data.url` | string |  |  |
| `purchase_details` | object |  | Additional purchase information that is optionally provided by the merchant. |
| `purchase_details.flight` | object |  |  |
| `purchase_details.flight.departure_at` | timestamp (Unix seconds) |  |  |
| `purchase_details.flight.passenger_name` | string |  |  |
| `purchase_details.flight.refundable` | boolean |  |  |
| `purchase_details.flight.segments` | array of object |  |  |
| `purchase_details.flight.segments[].arrival_airport_code` | string |  |  |
| `purchase_details.flight.segments[].carrier` | string |  |  |
| `purchase_details.flight.segments[].departure_airport_code` | string |  |  |
| `purchase_details.flight.segments[].flight_number` | string |  |  |
| `purchase_details.flight.segments[].service_class` | string |  |  |
| `purchase_details.flight.segments[].stopover_allowed` | boolean |  |  |
| `purchase_details.flight.travel_agency` | string |  |  |
| `purchase_details.fuel` | object |  |  |
| `purchase_details.fuel.type` | enum: `diesel`, `other`, `unleaded_plus`, `unleaded_regular`, `unleaded_super` |  |  |
| `purchase_details.fuel.unit` | enum: `liter`, `us_gallon` |  |  |
| `purchase_details.fuel.unit_cost_decimal` | string |  |  |
| `purchase_details.fuel.volume_decimal` | string |  |  |
| `purchase_details.lodging` | object |  |  |
| `purchase_details.lodging.check_in_at` | timestamp (Unix seconds) |  |  |
| `purchase_details.lodging.nights` | integer |  |  |
| `purchase_details.receipt` | array of object |  |  |
| `purchase_details.receipt[].description` | string |  |  |
| `purchase_details.receipt[].quantity` | string |  |  |
| `purchase_details.receipt[].total` | integer |  |  |
| `purchase_details.receipt[].unit_cost` | integer |  |  |
| `purchase_details.reference` | string |  |  |

Returns: `issuing.transaction`

## POST /v1/test_helpers/issuing/transactions/{transaction}/refund

operationId: `PostTestHelpersIssuingTransactionsTransactionRefund`

Refund a test-mode Transaction.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `transaction (path)` | string | yes |  |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `refund_amount` | integer |  | The total amount to attempt to refund. This amount is in the provided currency, or defaults to the cards currency, and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). |

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

