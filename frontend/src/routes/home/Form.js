import { h, Component } from "preact";

class ItineraryForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      locations: [],
      selectedLocation: null,
      priority: "3",
      time: "",
    };
    this.mapRef = null;
    this.autocomplete = null;
  }

  componentDidMount() {
    this.initMap();
  }

  initMap = () => {
    const google = window.google; // Ensure Google script is loaded
    this.mapRef = new google.maps.Map(document.getElementById("map"), {
      center: { lat: -34.397, lng: 150.644 },
      zoom: 8,
    });

    this.autocomplete = new google.maps.places.Autocomplete(
      document.getElementById("autocomplete")
    );
    this.autocomplete.bindTo("bounds", this.mapRef);
    this.autocomplete.addListener("place_changed", this.onPlaceSelected);
  };

  onPlaceSelected = () => {
    const place = this.autocomplete.getPlace();
    if (!place.geometry) {
      console.log("Returned place contains no geometry");
      return;
    }
    const location = {
      latitude: place.geometry.location.lat(),
      longitude: place.geometry.location.lng(),
      priority: "3",
      time: "",
    };
    this.setState({ selectedLocation: location });
  };

  addLocation = () => {
    this.setState((prevState) => ({
      locations: [...prevState.locations, prevState.selectedLocation],
      selectedLocation: null,
    }));
  };

  removeLocation = (index) => {
    this.setState((prevState) => ({
      locations: prevState.locations.filter((_, i) => i !== index),
    }));
  };

  handlePriorityChange = (event) => {
    this.setState({ priority: event.target.value });
  };

  handleTimeChange = (event) => {
    this.setState({ time: event.target.value });
  };

  handleSubmit = (event) => {
    event.preventDefault();
    // Process the form data
  };

  render() {
    return (
      <div>
        <div id="map" style={{ height: "300px" }}></div>
        <input id="autocomplete" type="text" placeholder="Enter a location" />
        <form onSubmit={this.handleSubmit}>
          <label>
            Priority:
            <select
              value={this.state.priority}
              onChange={this.handlePriorityChange}
            >
              <option value="1">1 - Highest</option>
              <option value="2">2</option>
              <option value="3">3 - Default</option>
              <option value="4">4</option>
              <option value="5">5 - Lowest</option>
            </select>
          </label>
          <label>
            Time:
            <input
              type="time"
              value={this.state.time}
              onChange={this.handleTimeChange}
            />
          </label>
          <button type="button" onClick={this.addLocation}>
            Add Location
          </button>
          <button type="submit">Submit Itinerary</button>
        </form>
        <ul>
          {this.state.locations.map((loc, index) => (
            <li key={index}>
              Latitude: {loc.latitude}, Longitude: {loc.longitude}, Priority:{" "}
              {loc.priority}, Time: {loc.time}
              <button onClick={() => this.removeLocation(index)}>Remove</button>
            </li>
          ))}
        </ul>
      </div>
    );
  }
}

export default ItineraryForm;
