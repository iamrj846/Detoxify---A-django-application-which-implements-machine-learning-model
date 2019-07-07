
function getLocation()
{
  // Obtain the initial location one-off
  navigator.geolocation.getCurrentPosition(getPosition);
}  

function getPosition(position)
{
  var location = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
  var mapOptions = {
	zoom : 12,
	center : location,
	mapTypeId : google.maps.MapTypeId.ROADMAP
  };
  var map = new google.maps.Map(document.getElementById('map-holder'), mapOptions);
  var marker = new google.maps.Marker({
	position: location,
	title: 'Here I am!',
	map: map,
	animation: google.maps.Animation.DROP
  });
  
  /* var geocoder = new google.maps.Geocoder();
  
  geocoder.geocode({
	  'latLng' : location
	}, 
	function(results, status) {
	  if (status == google.maps.GeocoderStatus.OK) {
		if (results[1]) {
		  var options = {
			  content : results[1].formatted_address,
			  position : location
		  };
		  var popup = new google.maps.InfoWindow(options);
		  google.maps.event.addListener(marker, 'click', function() {
			  popup.open(map);
		  });
		} 
		else 
		{
		  alert('No results found');
		}
	  } 
	  else 
	  {
		alert('Geocoder failed due to: ' + status);
	  }
	}
  ); */

    // Create the places service.
    var service = new google.maps.places.PlacesService(map);

    // Perform a nearby search.
    service.nearbySearch({
            location: location,
            radius: 4000,
            type: ['hospital']
        },
        function(results, status, pagination) {
            if (status !== 'OK') return;

            createMarkers(results);
            getNextPage = pagination.hasNextPage && function() {
                pagination.nextPage();
            };
        });
        function createMarkers(places) {
            var bounds = new google.maps.LatLngBounds();
            for (var i = 0, place; place = places[i]; i++) {
                var image = {
                    url: place.icon,
                    size: new google.maps.Size(71, 71),
                    origin: new google.maps.Point(0, 0),
                    anchor: new google.maps.Point(17, 34),
                    scaledSize: new google.maps.Size(25, 25)
                };
        
                var marker = new google.maps.Marker({
                    map: map,
                    icon: image,
                    title: place.name,
                    position: place.geometry.location
                });
                bounds.extend(place.geometry.location);
            }
            map.fitBounds(bounds);
        }


}














