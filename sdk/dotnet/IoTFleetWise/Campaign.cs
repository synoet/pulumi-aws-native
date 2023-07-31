// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTFleetWise
{
    /// <summary>
    /// Definition of AWS::IoTFleetWise::Campaign Resource Type
    /// </summary>
    [Obsolete(@"Campaign is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:iotfleetwise:Campaign")]
    public partial class Campaign : global::Pulumi.CustomResource
    {
        [Output("action")]
        public Output<Pulumi.AwsNative.IoTFleetWise.CampaignUpdateCampaignAction> Action { get; private set; } = null!;

        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("collectionScheme")]
        public Output<Union<Outputs.CollectionScheme0Properties, Outputs.CollectionScheme1Properties>> CollectionScheme { get; private set; } = null!;

        [Output("compression")]
        public Output<Pulumi.AwsNative.IoTFleetWise.CampaignCompression?> Compression { get; private set; } = null!;

        [Output("creationTime")]
        public Output<string> CreationTime { get; private set; } = null!;

        [Output("dataDestinationConfigs")]
        public Output<ImmutableArray<Union<Outputs.DataDestinationConfig0Properties, Outputs.DataDestinationConfig1Properties>>> DataDestinationConfigs { get; private set; } = null!;

        [Output("dataExtraDimensions")]
        public Output<ImmutableArray<string>> DataExtraDimensions { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("diagnosticsMode")]
        public Output<Pulumi.AwsNative.IoTFleetWise.CampaignDiagnosticsMode?> DiagnosticsMode { get; private set; } = null!;

        [Output("expiryTime")]
        public Output<string?> ExpiryTime { get; private set; } = null!;

        [Output("lastModificationTime")]
        public Output<string> LastModificationTime { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("postTriggerCollectionDuration")]
        public Output<double?> PostTriggerCollectionDuration { get; private set; } = null!;

        [Output("priority")]
        public Output<int?> Priority { get; private set; } = null!;

        [Output("signalCatalogArn")]
        public Output<string> SignalCatalogArn { get; private set; } = null!;

        [Output("signalsToCollect")]
        public Output<ImmutableArray<Outputs.CampaignSignalInformation>> SignalsToCollect { get; private set; } = null!;

        [Output("spoolingMode")]
        public Output<Pulumi.AwsNative.IoTFleetWise.CampaignSpoolingMode?> SpoolingMode { get; private set; } = null!;

        [Output("startTime")]
        public Output<string?> StartTime { get; private set; } = null!;

        [Output("status")]
        public Output<Pulumi.AwsNative.IoTFleetWise.CampaignStatus> Status { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.CampaignTag>> Tags { get; private set; } = null!;

        [Output("targetArn")]
        public Output<string> TargetArn { get; private set; } = null!;


        /// <summary>
        /// Create a Campaign resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Campaign(string name, CampaignArgs args, CustomResourceOptions? options = null)
            : base("aws-native:iotfleetwise:Campaign", name, args ?? new CampaignArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Campaign(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:iotfleetwise:Campaign", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Campaign resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Campaign Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Campaign(name, id, options);
        }
    }

    public sealed class CampaignArgs : global::Pulumi.ResourceArgs
    {
        [Input("action", required: true)]
        public Input<Pulumi.AwsNative.IoTFleetWise.CampaignUpdateCampaignAction> Action { get; set; } = null!;

        [Input("collectionScheme", required: true)]
        public InputUnion<Inputs.CollectionScheme0PropertiesArgs, Inputs.CollectionScheme1PropertiesArgs> CollectionScheme { get; set; } = null!;

        [Input("compression")]
        public Input<Pulumi.AwsNative.IoTFleetWise.CampaignCompression>? Compression { get; set; }

        [Input("dataDestinationConfigs")]
        private InputList<Union<Inputs.DataDestinationConfig0PropertiesArgs, Inputs.DataDestinationConfig1PropertiesArgs>>? _dataDestinationConfigs;
        public InputList<Union<Inputs.DataDestinationConfig0PropertiesArgs, Inputs.DataDestinationConfig1PropertiesArgs>> DataDestinationConfigs
        {
            get => _dataDestinationConfigs ?? (_dataDestinationConfigs = new InputList<Union<Inputs.DataDestinationConfig0PropertiesArgs, Inputs.DataDestinationConfig1PropertiesArgs>>());
            set => _dataDestinationConfigs = value;
        }

        [Input("dataExtraDimensions")]
        private InputList<string>? _dataExtraDimensions;
        public InputList<string> DataExtraDimensions
        {
            get => _dataExtraDimensions ?? (_dataExtraDimensions = new InputList<string>());
            set => _dataExtraDimensions = value;
        }

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("diagnosticsMode")]
        public Input<Pulumi.AwsNative.IoTFleetWise.CampaignDiagnosticsMode>? DiagnosticsMode { get; set; }

        [Input("expiryTime")]
        public Input<string>? ExpiryTime { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("postTriggerCollectionDuration")]
        public Input<double>? PostTriggerCollectionDuration { get; set; }

        [Input("priority")]
        public Input<int>? Priority { get; set; }

        [Input("signalCatalogArn", required: true)]
        public Input<string> SignalCatalogArn { get; set; } = null!;

        [Input("signalsToCollect")]
        private InputList<Inputs.CampaignSignalInformationArgs>? _signalsToCollect;
        public InputList<Inputs.CampaignSignalInformationArgs> SignalsToCollect
        {
            get => _signalsToCollect ?? (_signalsToCollect = new InputList<Inputs.CampaignSignalInformationArgs>());
            set => _signalsToCollect = value;
        }

        [Input("spoolingMode")]
        public Input<Pulumi.AwsNative.IoTFleetWise.CampaignSpoolingMode>? SpoolingMode { get; set; }

        [Input("startTime")]
        public Input<string>? StartTime { get; set; }

        [Input("tags")]
        private InputList<Inputs.CampaignTagArgs>? _tags;
        public InputList<Inputs.CampaignTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.CampaignTagArgs>());
            set => _tags = value;
        }

        [Input("targetArn", required: true)]
        public Input<string> TargetArn { get; set; } = null!;

        public CampaignArgs()
        {
        }
        public static new CampaignArgs Empty => new CampaignArgs();
    }
}
