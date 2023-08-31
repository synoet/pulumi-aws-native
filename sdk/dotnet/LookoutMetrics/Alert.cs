// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.LookoutMetrics
{
    /// <summary>
    /// Resource Type definition for AWS::LookoutMetrics::Alert
    /// </summary>
    [AwsNativeResourceType("aws-native:lookoutmetrics:Alert")]
    public partial class Alert : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The action to be taken by the alert when an anomaly is detected.
        /// </summary>
        [Output("action")]
        public Output<Outputs.AlertAction> Action { get; private set; } = null!;

        /// <summary>
        /// A description for the alert.
        /// </summary>
        [Output("alertDescription")]
        public Output<string?> AlertDescription { get; private set; } = null!;

        /// <summary>
        /// The name of the alert. If not provided, a name is generated automatically.
        /// </summary>
        [Output("alertName")]
        public Output<string?> AlertName { get; private set; } = null!;

        /// <summary>
        /// A number between 0 and 100 (inclusive) that tunes the sensitivity of the alert.
        /// </summary>
        [Output("alertSensitivityThreshold")]
        public Output<int> AlertSensitivityThreshold { get; private set; } = null!;

        /// <summary>
        /// The Amazon resource name (ARN) of the Anomaly Detector to alert.
        /// </summary>
        [Output("anomalyDetectorArn")]
        public Output<string> AnomalyDetectorArn { get; private set; } = null!;

        /// <summary>
        /// ARN assigned to the alert.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;


        /// <summary>
        /// Create a Alert resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Alert(string name, AlertArgs args, CustomResourceOptions? options = null)
            : base("aws-native:lookoutmetrics:Alert", name, args ?? new AlertArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Alert(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:lookoutmetrics:Alert", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "action",
                    "alertDescription",
                    "alertName",
                    "alertSensitivityThreshold",
                    "anomalyDetectorArn",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Alert resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Alert Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Alert(name, id, options);
        }
    }

    public sealed class AlertArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The action to be taken by the alert when an anomaly is detected.
        /// </summary>
        [Input("action", required: true)]
        public Input<Inputs.AlertActionArgs> Action { get; set; } = null!;

        /// <summary>
        /// A description for the alert.
        /// </summary>
        [Input("alertDescription")]
        public Input<string>? AlertDescription { get; set; }

        /// <summary>
        /// The name of the alert. If not provided, a name is generated automatically.
        /// </summary>
        [Input("alertName")]
        public Input<string>? AlertName { get; set; }

        /// <summary>
        /// A number between 0 and 100 (inclusive) that tunes the sensitivity of the alert.
        /// </summary>
        [Input("alertSensitivityThreshold", required: true)]
        public Input<int> AlertSensitivityThreshold { get; set; } = null!;

        /// <summary>
        /// The Amazon resource name (ARN) of the Anomaly Detector to alert.
        /// </summary>
        [Input("anomalyDetectorArn", required: true)]
        public Input<string> AnomalyDetectorArn { get; set; } = null!;

        public AlertArgs()
        {
        }
        public static new AlertArgs Empty => new AlertArgs();
    }
}
