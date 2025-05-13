import React, { useState } from "react";
import "../styles/ReportViewer.css";
import axios from "axios";
import { API_URL } from "../config/constants";

const ReportViewer = ({ report, isLoading }) => {
  const [exportFormat, setExportFormat] = useState("pdf");
  const [showEmailForm, setShowEmailForm] = useState(false);
  const [emailData, setEmailData] = useState({
    patient_email: "",
    patient_name: "",
  });
  const [emailStatus, setEmailStatus] = useState({
    sending: false,
    success: false,
    error: null,
  });

  const handleExport = async () => {
    if (!report) return;

    try {
      // Use the base64 data directly from the report
      const base64Data = report[exportFormat];
      if (!base64Data) {
        console.error("No data available for the selected format");
        return;
      }

      // Convert base64 to blob
      const byteCharacters = atob(base64Data);
      const byteNumbers = new Array(byteCharacters.length);
      for (let i = 0; i < byteCharacters.length; i++) {
        byteNumbers[i] = byteCharacters.charCodeAt(i);
      }
      const byteArray = new Uint8Array(byteNumbers);
      const blob = new Blob([byteArray], {
        type: `application/${exportFormat}`,
      });

      // Create download link
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = `medical-report.${exportFormat}`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      window.URL.revokeObjectURL(url);
    } catch (error) {
      console.error("Error downloading report:", error);
    }
  };

  const handleEmailFormChange = (e) => {
    const { name, value } = e.target;
    setEmailData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSendEmail = async (e) => {
    e.preventDefault();
    if (!report) return;

    setEmailStatus({ sending: true, success: false, error: null });

    try {
      // Utiliser authToken au lieu de token
      const token = localStorage.getItem("authToken");
      await axios.post(
        `${API_URL}/reports/send-email/`,
        {
          report_id: report.report_id,
          patient_email: emailData.patient_email,
          patient_name: emailData.patient_name,
          format: exportFormat,
        },
        {
          headers: {
            // Utiliser Token au lieu de Bearer
            Authorization: `Token ${token}`,
          },
        }
      );

      setEmailStatus({
        sending: false,
        success: true,
        error: null,
      });

      // Reset form after successful send
      setTimeout(() => {
        setShowEmailForm(false);
        setEmailData({ patient_email: "", patient_name: "" });
        setEmailStatus({ sending: false, success: false, error: null });
      }, 3000);
    } catch (error) {
      console.error("Error sending report by email:", error);
      setEmailStatus({
        sending: false,
        success: false,
        error: error.response?.data?.error || "Failed to send email",
      });
    }
  };

  if (isLoading) {
    return (
      <div className="report-viewer">
        <div className="loading-container">
          <div className="loading-spinner"></div>
          <p>Generating medical report...</p>
          <p className="loading-note">
            This may take a moment as we analyze the image and prepare a
            detailed report.
          </p>
        </div>
      </div>
    );
  }

  if (!report) {
    return (
      <div className="report-viewer empty-viewer">
        <div className="placeholder-content">
          <i className="report-icon">📋</i>
          <h3>No Report Generated</h3>
          <p>
            Upload a medical image and click "Generate Report" to view results
            here.
          </p>
        </div>
      </div>
    );
  }

  return (
    <div className="report-viewer">
      <div className="report-header">
        <h2>Medical Analysis Report</h2>
        <div className="export-controls">
          <select
            value={exportFormat}
            onChange={(e) => setExportFormat(e.target.value)}
          >
            <option value="pdf">PDF Format</option>
            <option value="docx">Word Document</option>
          </select>
          <button onClick={handleExport} className="export-button">
            Download Report
          </button>
          <button
            onClick={() => setShowEmailForm(!showEmailForm)}
            className="email-button"
          >
            Send by Email
          </button>
        </div>
      </div>

      {showEmailForm && (
        <div className="email-form-container">
          <form onSubmit={handleSendEmail} className="email-form">
            <h3>Send Report to Patient</h3>
            <div className="form-group">
              <label htmlFor="patient_name">Patient Name:</label>
              <input
                type="text"
                id="patient_name"
                name="patient_name"
                value={emailData.patient_name}
                onChange={handleEmailFormChange}
                required
              />
            </div>
            <div className="form-group">
              <label htmlFor="patient_email">Patient Email:</label>
              <input
                type="email"
                id="patient_email"
                name="patient_email"
                value={emailData.patient_email}
                onChange={handleEmailFormChange}
                required
              />
            </div>
            <div className="form-group">
              <label>Format:</label>
              <span>{exportFormat.toUpperCase()}</span>
            </div>
            <div className="form-actions">
              <button
                type="button"
                onClick={() => setShowEmailForm(false)}
                className="cancel-button"
              >
                Cancel
              </button>
              <button
                type="submit"
                className="send-button"
                disabled={emailStatus.sending}
              >
                {emailStatus.sending ? "Sending..." : "Send Report"}
              </button>
            </div>
            {emailStatus.success && (
              <div className="success-message">Report sent successfully!</div>
            )}
            {emailStatus.error && (
              <div className="error-message">{emailStatus.error}</div>
            )}
          </form>
        </div>
      )}

      <div className="report-content">
        <div className="report-section">
          <h3>Diagnosis Summary</h3>
          <p>{report.diagnosis || "No diagnosis available"}</p>
        </div>

        <div className="report-section">
          <h3>Analysis Details</h3>
          <div className="accuracy-meter">
            <div className="accuracy-label">
              Model Confidence: {(report.accuracy * 100).toFixed(1)}%
            </div>
            <div className="accuracy-bar">
              <div
                className="accuracy-fill"
                style={{ width: `${report.accuracy * 100}%` }}
              ></div>
            </div>
          </div>
          <div className="condition-details">
            <p>{report.details || "No detailed analysis available"}</p>
          </div>
        </div>

        <div className="report-section">
          <h3>Treatment Recommendations</h3>
          {report.recommendations && report.recommendations.length > 0 ? (
            <ul className="recommendations-list">
              {report.recommendations.map((rec, index) => (
                <li key={index}>{rec}</li>
              ))}
            </ul>
          ) : (
            <p>No specific recommendations available</p>
          )}
        </div>

        <div className="report-footer">
          <p>Report ID: {report.report_id}</p>
        </div>
      </div>
    </div>
  );
};

export default ReportViewer;
