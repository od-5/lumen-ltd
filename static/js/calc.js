/**
 * Created by alexy on 11.09.15.
 */
$(function(){
  var power = 1;
  var n_power = 1;
  var lamp_count = 1;
  var drossel_power = 0;
  $('.calculator-form button').click(function(){
    var type = parseInt($('#c-type').val());
    //if (type==1) {
    //  var power = 18;
    //  var n_power = 6.5;
    //  var lamp_count = 1
    //}
    switch (type) {
      case 1:
        power = 18;
        n_power = 6.5;
        lamp_count = 1;
        break;
      case 2:
        power = 36;
        n_power = 13;
        lamp_count = 1;
        break;
      case 3:
        power = 58;
        n_power = 25;
        lamp_count = 1;
        break;
      case 4:
        power = 25;
        n_power = 6;
        lamp_count = 1;
        break;
      default:
        alert('Я таких значений не знаю')
    }

    var hours = parseInt($('#c-hours').val());
    var days = parseInt($('#c-days').val());
    var quantity = parseInt($('#c-quantity').val());
    if (type==4 || type==5) {
      drossel_power = 0;
    } else {
      drossel_power = (power * lamp_count) * 0.1;
    }
    var total_power = drossel_power + (power * lamp_count);
    var n_total_power = n_power * lamp_count;

    var h_power = (total_power /1000) * quantity;
    var n_h_power = (n_total_power /1000) * quantity;
    var d_power = h_power * hours;
    var n_d_power = n_h_power * hours;
    var m_power = d_power * days;
    var n_m_power = n_d_power * days;
    var y_power = m_power * 12;
    var n_y_power = n_m_power * 12;
    var y3_power = y_power * 3;
    var n_y3_power = n_y_power * 3;

    var hour_economy_p = h_power - n_h_power;
    var day_economy_p = d_power - n_d_power;
    var month_economy_p = m_power - n_m_power;
    var year_economy_p = y_power - n_y_power;
    var year3_economy_p = y3_power - n_y3_power;

    var hour_economy_r = hour_economy_p * 5;
    var day_economy_r = day_economy_p * 5;
    var month_economy_r = month_economy_p * 5;
    var year_economy_r = year_economy_p * 5;
    var year3_economy_r = year3_economy_p *5;
    $('#hour_economy_watt').text(hour_economy_p.toFixed(2));
    $('#hour_economy_rub').text(hour_economy_r.toFixed(2));

    $('#day_economy_watt').text(day_economy_p.toFixed(2));
    $('#day_economy_rub').text(day_economy_r.toFixed(2));

    $('#month_economy_watt').text(month_economy_p.toFixed(2));
    $('#month_economy_rub').text(month_economy_r.toFixed(2));

    $('#year_economy_watt').text(year_economy_p.toFixed(2));
    $('#year_economy_rub').text(year_economy_r.toFixed(2));

    $('#year3_economy_watt').text(year3_economy_p.toFixed(2));
    $('#year3_economy_rub').text(year3_economy_r.toFixed(2));


  })
});