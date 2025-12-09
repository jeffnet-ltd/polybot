/**
 * FlagIcon Component
 * Displays flag SVG from FlagCDN
 */

const FlagIcon = ({ countryCode, className = "w-5 h-4" }) => (
    <img
        src={`https://flagcdn.com/${countryCode}.svg`}
        alt={countryCode}
        className={`object-cover rounded-sm border border-gray-200 ${className}`}
    />
);

export default FlagIcon;
