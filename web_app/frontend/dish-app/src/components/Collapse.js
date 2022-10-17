import React from 'react';
const Collapse = ({ collapsed, children, country }) => {
    const [isCollapsed, setIsCollapsed] = React.useState(collapsed);
  
    return (
      <>
        <button
          className="collapse-button"
          onClick={() => setIsCollapsed(!isCollapsed)}
        >
          {isCollapsed ? '' : 'Hide'} {country.name}
        </button>
        <div
          className={`collapse-content ${isCollapsed ? 'collapsed' : 'expanded'}`}
          aria-expanded={isCollapsed}
        >
          {children}
        </div>
      </>
    );
  };


export default Collapse;