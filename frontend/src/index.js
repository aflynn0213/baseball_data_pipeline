// Import necessary libraries
import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router } from 'react-router-dom';
import App from './App'; // Your main App component
import { ThemeProvider } from './context/ThemeContext'; // Context for theming
import ErrorBoundary from './components/ErrorBoundary'; // Error boundary component
import GlobalStyles from './styles/GlobalStyles'; // Global CSS styles
import * as serviceWorker from './serviceWorker'; // Service worker for offline capabilities
import { AnalyticsProvider } from './context/AnalyticsContext'; // Custom analytics context

// Render the App component
ReactDOM.render(
  <React.StrictMode>
    <ThemeProvider>
      <AnalyticsProvider>
        <Router>
          <ErrorBoundary>
            <GlobalStyles />
            <App />
          </ErrorBoundary>
        </Router>
      </AnalyticsProvider>
    </ThemeProvider>
  </React.StrictMode>,
  document.getElementById('root')
);

// Register service worker for offline support
serviceWorker.register();
