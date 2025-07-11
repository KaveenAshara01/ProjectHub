
import React from "react";

const ProjectCard = ({ project, onView, onDelete }) => {
  return (
    <div className="bg-white shadow rounded-2xl p-4 flex flex-col justify-between">
      <div>
        <h2 className="text-xl font-semibold">{project.title}</h2>
        <p className="text-sm text-gray-600 mt-1">{project.description}</p>
        <p className="text-xs text-gray-400 mt-2">
          Created on: {new Date(project.created_at).toLocaleDateString()}
        </p>
      </div>
      <div className="flex gap-2 mt-4">
        <button
          onClick={() => onView(project)}
          className="bg-blue-600 text-white px-3 py-1 rounded-xl hover:bg-blue-700"
        >
          View Tasks
        </button>
        <button
          onClick={() => onDelete(project.id)}
          className="bg-red-500 text-white px-3 py-1 rounded-xl hover:bg-red-600"
        >
          Delete
        </button>
      </div>
    </div>
  );
};

export default ProjectCard ;
