/**
 * ProgressCard Component
 * Displays a statistic card with icon, title, and value
 */

const ProgressCard = ({ icon: Icon, title, value, color }) => (
    <div className="flex items-center justify-between p-3 bg-white rounded-xl shadow-lg border border-gray-100 transition duration-300 hover:shadow-xl">
        <div className={`p-2 rounded-full text-white ${color}`}>
            <Icon size={20} />
        </div>
        <div className="text-right">
            <p className="text-xs text-gray-500 font-medium">{title}</p>
            <p className="text-2xl font-bold text-gray-800">{value}</p>
        </div>
    </div>
);

export default ProgressCard;
