from pages.block_with_ordering_a_taxi import BlockWithOrderingATaxi
from pages.block_with_choosing_route import BlockWithChoosingRoute
import allure
import pytest
from locators.tariffe_picker_block_locators import TariffPickerBlockLocators
from data import InfoAboutTariffs


class TestBlockWIthOrderingATaxi:

     @allure.title('Проверка появления 6 тарифов и один из них активный при клике на кнопку вызова такси')
     def test_six_tariffs_opens_and_faster_is_active_after_click_to_button_to_get_a_taxi(self, driver, fill_started_block):
         bwoat = BlockWithOrderingATaxi(driver)
         bwcar = BlockWithChoosingRoute(driver)

         bwcar.click_to_the_button_call_a_taxi()

         assert (bwoat.check_displaying_active_tariff_worker and
                 bwoat.check_displaying_non_active_tariff_glantsevi and
                 bwoat.check_displaying_non_active_tariff_razgovorchivi and
                 bwoat.check_displaying_non_active_tariff_uteshitelni and
                 bwoat.check_displaying_non_active_tariff_otpusknoi and
                 bwoat.check_displaying_non_active_tariff_sonni)

     @allure.title('Проверка отображения инфо о тарифе и заголовка при наведении курсора на иконку i')
     @pytest.mark.xfail
     @pytest.mark.parametrize('locator, true_title, true_descr',
             [(TariffPickerBlockLocators.ACTIVE_CARD_WORKER,
               InfoAboutTariffs.title_worker,
               InfoAboutTariffs.descr_worker),
              (TariffPickerBlockLocators.NONE_ACTIVE_CARD_GLANTSEVI,
               InfoAboutTariffs.title_glantsevi,
               InfoAboutTariffs.descr_glantsevi),
              (TariffPickerBlockLocators.NONE_ACTIVE_CARD_OTPUSKNOI,
               InfoAboutTariffs.title_otpusknoi,
               InfoAboutTariffs.descr_otpusknoi),
              (TariffPickerBlockLocators.NONE_ACTIVE_CARD_UTESHITELNI,
               InfoAboutTariffs.title_uteshitelni,
               InfoAboutTariffs.descr_uteshitelni),
              (TariffPickerBlockLocators.NONE_ACTIVE_CARD_SONNI,
               InfoAboutTariffs.title_sonni,
               InfoAboutTariffs.descr_sonni),
              (TariffPickerBlockLocators.NONE_ACTIVE_CARD_RAZGOVORCHIVI,
               InfoAboutTariffs.title_razgovorchivi,
               InfoAboutTariffs.descr_razgovorchivi)
              ]
     )
     def test_info_about_tariff_is_true_after_move_to_i_icon(self, driver, fill_started_block, locator, true_title, true_descr):
         bwoat = BlockWithOrderingATaxi(driver)
         bwcar = BlockWithChoosingRoute(driver)

         bwcar.click_to_the_button_call_a_taxi()
         bwoat.click_to_tariff(locator)
         bwoat.move_to_i_in_tariff()
         title = bwoat.get_text_from_title_about_tariff()
         description = bwoat.get_text_from_descr_about_tariff()

         assert title == true_title and description == true_descr

     @allure.title('Проверка отображения поля телефон, требования к заказу, способа оплаты, комментария и кнопки вызова такси')
     @pytest.mark.parametrize('scrolling_to, check_displaying',
                              (
                                      (BlockWithOrderingATaxi.scrolling_to_the_button_order_taxi,
                                       BlockWithOrderingATaxi.check_displaying_button_order_taxi),
                                      (BlockWithOrderingATaxi.scrolling_to_block_req_to_the_order,
                                       BlockWithOrderingATaxi.check_displaying_block_req_to_the_order),
                                      (BlockWithOrderingATaxi.scrolling_to_field_method_of_paying,
                                       BlockWithOrderingATaxi.check_displaying_payment_method),
                                      (BlockWithOrderingATaxi.scrolling_to_field_phone,
                                       BlockWithOrderingATaxi.check_displaying_input_telephone),
                                      (BlockWithOrderingATaxi.scrolling_to_input_comment,
                                       BlockWithOrderingATaxi.check_displaying_input_comment)
     )
                              )
     def test_check_displaying_fields_telephone_pay_method_comments_and_req_to_order(self, driver, fill_started_block, scrolling_to, check_displaying):
         bwoat = BlockWithOrderingATaxi(driver)
         bwcar = BlockWithChoosingRoute(driver)

         bwcar.click_to_the_button_call_a_taxi()
         scrolling_to(bwoat)

         assert check_displaying(bwoat)