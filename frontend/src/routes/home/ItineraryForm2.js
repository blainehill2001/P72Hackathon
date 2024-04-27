import { useState, useEffect } from "preact/hooks";
import { Loader } from "@googlemaps/js-api-loader";

const ItineraryForm2 = () => {
  const [locations, setLocations] = useState([]);
  const [apiResponse, setApiResponse] = useState(null);
  const [autocomplete, setAutocomplete] = useState(null);

  useEffect(() => {
    const loader = new Loader({
      apiKey: "YOUR_API_KEY", // unable to get currently
      libraries: ["places"],
    });

    loader.load().then(() => {
      const input = document.getElementById("autocomplete");
      const autocompleteInstance = new google.maps.places.Autocomplete(input);
      autocompleteInstance.addListener("place_changed", () => {
        const place = autocompleteInstance.getPlace();
        if (!place.geometry) {
          console.log("Returned place contains no geometry");
          return;
        }
        const locationData = {
          name: place.name,
          lat: place.geometry.location.lat() || 0,
          lng: place.geometry.location.lng() || 0,
          priority: 3, // default priority
          time: undefined, // default time
        };
        setLocations([...locations, locationData]);
      });
      setAutocomplete(autocompleteInstance);
    });
  }, []);

  const handleRemoveLocation = (index) => {
    const updatedLocations = locations.filter((_, idx) => idx !== index);
    setLocations(updatedLocations);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const apiUrl = "http://127.0.0.1:5000/algo";
    console.log(JSON.stringify({ locations }));

    fetch(apiUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ locations }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Success:", data);
        setApiResponse(data);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Location:
          <input id="autocomplete" type="text" placeholder="Enter a location" />
        </label>
        <button type="submit">Submit Itinerary</button>
      </form>
      <ul>
        {locations.map((loc, index) => (
          <li key={index}>
            {loc.name} - Lat: {loc.lat}, Lng: {loc.lng} - Priority:{" "}
            {loc.priority} - Time: {loc.time || "Anytime"}
            <button onClick={() => handleRemoveLocation(index)}>Remove</button>
          </li>
        ))}
      </ul>
      {apiResponse && <div>Response: {JSON.stringify(apiResponse)}</div>}
    </div>
  );
};

export default ItineraryForm22;
