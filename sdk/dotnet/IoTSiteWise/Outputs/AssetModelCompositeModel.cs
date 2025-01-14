// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTSiteWise.Outputs
{

    /// <summary>
    /// Contains a composite model definition in an asset model. This composite model definition is applied to all assets created from the asset model.
    /// </summary>
    [OutputType]
    public sealed class AssetModelCompositeModel
    {
        /// <summary>
        /// The property definitions of the asset model. You can specify up to 200 properties per asset model.
        /// </summary>
        public readonly ImmutableArray<Outputs.AssetModelProperty> CompositeModelProperties;
        /// <summary>
        /// A description for the asset composite model.
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// A unique, friendly name for the asset composite model.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The type of the composite model. For alarm composite models, this type is AWS/ALARM
        /// </summary>
        public readonly string Type;

        [OutputConstructor]
        private AssetModelCompositeModel(
            ImmutableArray<Outputs.AssetModelProperty> compositeModelProperties,

            string? description,

            string name,

            string type)
        {
            CompositeModelProperties = compositeModelProperties;
            Description = description;
            Name = name;
            Type = type;
        }
    }
}
