import { useState } from "preact/hooks";

const ItineraryForm = () => {
  const [locations, setLocations] = useState([]);
  const [newLocation, setNewLocation] = useState("");
  const [priority, setPriority] = useState(3);
  const [visitTime, setVisitTime] = useState("");
  const [apiResponse, setApiResponse] = useState(null); // State to store API response

  const handleAddLocation = () => {
    const locationData = {
      name: newLocation,
      priority: priority,
      time: visitTime || undefined,
    };
    setLocations([...locations, locationData]);
    setNewLocation("");
    setPriority(3);
    setVisitTime("");
  };

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
      .then((response) => {
        console.log(response);

        response.json();
      })
      .then((data) => {
        console.log("Success:", data);
        setApiResponse(data); // Update state with the API response
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
          <input
            type="text"
            value={newLocation}
            onChange={(e) => setNewLocation(e.target.value)}
          />
        </label>
        <label>
          Priority (1-5):
          <input
            type="number"
            min="1"
            max="5"
            value={priority}
            onChange={(e) => setPriority(parseInt(e.target.value))}
          />
        </label>
        <label>
          Visit Time (optional):
          <input
            type="time"
            value={visitTime}
            onChange={(e) => setVisitTime(e.target.value)}
          />
        </label>
        <button type="button" onClick={handleAddLocation}>
          Add Location
        </button>
        <button type="submit">Submit Itinerary</button>
      </form>
      <ul>
        {locations.map((loc, index) => (
          <li key={index}>
            {loc.name} - Priority: {loc.priority} - Time:{" "}
            {loc.time || "Anytime"}
            <button onClick={() => handleRemoveLocation(index)}>Remove</button>
          </li>
        ))}
      </ul>
      {apiResponse && <div>Response: {JSON.stringify(apiResponse)}</div>}
    </div>
  );
};

export default ItineraryForm;
