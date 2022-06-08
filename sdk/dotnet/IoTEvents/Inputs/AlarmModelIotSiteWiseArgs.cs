// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTEvents.Inputs
{

    /// <summary>
    /// Sends information about the alarm model instance and the event that triggered the action to a specified asset property in AWS IoT SiteWise.
    /// </summary>
    public sealed class AlarmModelIotSiteWiseArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the asset that has the specified property. You can specify an expression.
        /// </summary>
        [Input("assetId")]
        public Input<string>? AssetId { get; set; }

        /// <summary>
        /// A unique identifier for this entry. You can use the entry ID to track which data entry causes an error in case of failure. The default is a new unique identifier. You can also specify an expression.
        /// </summary>
        [Input("entryId")]
        public Input<string>? EntryId { get; set; }

        /// <summary>
        /// The alias of the asset property. You can also specify an expression.
        /// </summary>
        [Input("propertyAlias")]
        public Input<string>? PropertyAlias { get; set; }

        /// <summary>
        /// The ID of the asset property. You can specify an expression.
        /// </summary>
        [Input("propertyId")]
        public Input<string>? PropertyId { get; set; }

        [Input("propertyValue")]
        public Input<Inputs.AlarmModelAssetPropertyValueArgs>? PropertyValue { get; set; }

        public AlarmModelIotSiteWiseArgs()
        {
        }
    }
}
