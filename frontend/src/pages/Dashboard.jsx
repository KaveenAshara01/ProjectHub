import { useEffect, useState } from "react";
import { fetchProjects, deleteProject } from "../api/projectApi";
import ProjectCard from "../components/ProjectCard";
import { useAuth } from "../context/AuthContext";

const Dashboard = () => {
  const { user, logout } = useAuth();
  const [projects, setProjects] = useState([]);

  const loadProjects = async () => {
    try {
      const data = await fetchProjects();
      setProjects(data);
    } catch (err) {
      console.error("Failed to load projects:", err);
    }
  };

  const handleDelete = async (id) => {
    await deleteProject(id);
    setProjects((prev) => prev.filter((p) => p.id !== id));
  };

  const handleView = (project) => {
    console.log("Viewing tasks for project:", project);
    // Later: open modal or navigate to /tasks/:id
  };

  useEffect(() => {
    loadProjects();
  }, []);

  return (
    <div className="min-h-screen bg-white text-gray-800 p-6">
      <div className="mb-6">
        <h1 className="text-3xl font-bold">👤 Member Dashboard</h1>
        <p className="mt-2">
          Welcome, <span className="font-semibold">{user?.username}</span>!
        </p>
        <p>
          Your role is:{" "}
          <span className="text-green-600 font-medium">{user?.role}</span>
        </p>
        <button
          onClick={logout}
          className="mt-4 px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700"
        >
          Logout
        </button>
      </div>

      <h2 className="text-2xl font-semibold mb-4">Your Projects</h2>
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
        {projects.map((project) => (
          <ProjectCard
            key={project.id}
            project={project}
            onView={handleView}
            onDelete={handleDelete}
          />
        ))}
      </div>
    </div>
  );
};

export default Dashboard;
