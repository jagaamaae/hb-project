// Replace this with your code
const form = $('#get-country');

form.on('submit', (evt) => {
    evt.preventDefault();
    let country =  $('#country-id option:selected').val()
    console.log(country)
    $.get(`/most_affected_details/${country}`, (res) => {
        $('#country').html(res.country);
        $('#population').html(res.population);
        $('.link').attr("href", `/countries/${country}`)
      });
  });
