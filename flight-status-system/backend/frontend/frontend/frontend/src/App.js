import React from 'react';
import FlightStatus from './components/FlightStatus';
import NotificationSettings from './components/NotificationSettings';

function App() {
    return ( <
        div className = "App" >
        <
        header className = "App-header" >
        <
        h1 > Flight Status and Notifications < /h1> <
        /header> <
        FlightStatus / >
        <
        NotificationSettings / >
        <
        /div>
    );
}

export default App;