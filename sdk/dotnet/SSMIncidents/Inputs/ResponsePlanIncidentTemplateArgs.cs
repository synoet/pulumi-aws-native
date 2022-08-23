// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SSMIncidents.Inputs
{

    /// <summary>
    /// The incident template configuration.
    /// </summary>
    public sealed class ResponsePlanIncidentTemplateArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The deduplication string.
        /// </summary>
        [Input("dedupeString")]
        public Input<string>? DedupeString { get; set; }

        /// <summary>
        /// The impact value.
        /// </summary>
        [Input("impact", required: true)]
        public Input<int> Impact { get; set; } = null!;

        [Input("incidentTags")]
        private InputList<Inputs.ResponsePlanTagArgs>? _incidentTags;

        /// <summary>
        /// Tags that get applied to incidents created by the StartIncident API action.
        /// </summary>
        public InputList<Inputs.ResponsePlanTagArgs> IncidentTags
        {
            get => _incidentTags ?? (_incidentTags = new InputList<Inputs.ResponsePlanTagArgs>());
            set => _incidentTags = value;
        }

        [Input("notificationTargets")]
        private InputList<Inputs.ResponsePlanNotificationTargetItemArgs>? _notificationTargets;

        /// <summary>
        /// The list of notification targets.
        /// </summary>
        public InputList<Inputs.ResponsePlanNotificationTargetItemArgs> NotificationTargets
        {
            get => _notificationTargets ?? (_notificationTargets = new InputList<Inputs.ResponsePlanNotificationTargetItemArgs>());
            set => _notificationTargets = value;
        }

        /// <summary>
        /// The summary string.
        /// </summary>
        [Input("summary")]
        public Input<string>? Summary { get; set; }

        /// <summary>
        /// The title string.
        /// </summary>
        [Input("title", required: true)]
        public Input<string> Title { get; set; } = null!;

        public ResponsePlanIncidentTemplateArgs()
        {
        }
        public static new ResponsePlanIncidentTemplateArgs Empty => new ResponsePlanIncidentTemplateArgs();
    }
}
