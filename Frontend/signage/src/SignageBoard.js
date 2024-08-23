import React, { useEffect, useState } from 'react';

const SignageBoard = () => {
    const [currentToken, setCurrentToken] = useState(null);

    useEffect(() => {
        const fetchCurrentToken = async () => {
            try {
          //       const data = {};
                const response = await fetch('http://localhost:8000/fetch-token/',
                     {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json'
                            },
                    //        body: JSON.stringify(data) // Convert your data to JSON format
                });
                const resdata = await response.json();
                 console.log('Response data:', resdata);
                 console.log('Response data:', resdata.Token_number);// Log the response data for debugging

                setCurrentToken(resdata.Token_number);
            } catch (error) {
                console.error('Error fetching current token:', error);
            }
        };

        fetchCurrentToken();
        const intervalId = setInterval(fetchCurrentToken, 15000); // Refresh every 5 seconds

        return () => clearInterval(intervalId);
    }, []);

    return (
        <div style={{ textAlign: 'center', marginTop: '50px' }}>
            <h1>Now Serving</h1>
            <h2>{currentToken ? currentToken : 'Loading...'}</h2>
        </div>
    );
};

export default SignageBoard;
