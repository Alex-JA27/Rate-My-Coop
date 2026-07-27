import { useState } from "react";

// Fake data lives right here for now — no separate file needed
const coops = [
  {
    id: 1,
    company: "Fidelity Investments",
    role: "Software Engineer Co-op",
    location: "Boston, MA",
    overall: 4.5,
    wouldRecommend: 90,
    workload: 3.5,
    reviewsCount: 2,
  },
  {
    id: 2,
    company: "Wayfair",
    role: "Data Analyst Co-op",
    location: "Boston, MA",
    overall: 3.5,
    wouldRecommend: 70,
    workload: 4,
    reviewsCount: 1,
  },
  {
    id: 3,
    company: "MathWorks",
    role: "QA Engineering Co-op",
    location: "Natick, MA",
    overall: 4,
    wouldRecommend: 85,
    workload: 3,
    reviewsCount: 1,
  },
];

export default function HomePage() {
  const [search, setSearch] = useState("");

  const filtered = coops.filter((coop) => {
    const text = (coop.company + coop.role).toLowerCase();
    return text.includes(search.toLowerCase());
  });

  return (
    <div>
      {/* Hero band */}
      <div className="bg-neutral-900 text-white py-20 px-6 text-center">
        <h1 className="text-4xl sm:text-5xl font-bold mb-6">
          Find a <span className="text-red-500">co-op</span> at Northeastern
        </h1>
        <input
          type="text"
          placeholder="Search by company or role..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          className="w-full max-w-xl mx-auto block rounded-full px-6 py-3 text-black"
        />
      </div>

      {/* Results list */}
      <div className="max-w-3xl mx-auto p-6 space-y-4">
        {filtered.map((coop) => (
          <div
            key={coop.id}
            className="flex gap-4 bg-gray-50 hover:bg-gray-100 rounded-lg p-4 transition"
          >
            {/* Green quality score box */}
            <div className="flex flex-col items-center justify-center shrink-0">
              <span className="text-xs font-semibold text-gray-500">QUALITY</span>
              <div className="bg-green-300 text-black text-3xl font-bold w-20 h-20 flex items-center justify-center rounded">
                {coop.overall.toFixed(1)}
              </div>
              <span className="text-xs text-gray-500 mt-1">{coop.reviewsCount} ratings</span>
            </div>

            {/* Info */}
            <div className="flex-1">
              <h2 className="text-2xl font-bold">{coop.company}</h2>
              <p className="text-gray-700">{coop.role}</p>
              <p className="text-gray-500">{coop.location}</p>
              <p className="mt-3 text-sm">
                <span className="font-bold">{coop.wouldRecommend}%</span> would recommend
                <span className="mx-2 text-gray-300">|</span>
                <span className="font-bold">{coop.workload}</span> workload
              </p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}