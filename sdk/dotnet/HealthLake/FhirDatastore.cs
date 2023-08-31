// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.HealthLake
{
    /// <summary>
    /// HealthLake FHIR Datastore
    /// </summary>
    [AwsNativeResourceType("aws-native:healthlake:FhirDatastore")]
    public partial class FhirDatastore : global::Pulumi.CustomResource
    {
        [Output("createdAt")]
        public Output<Outputs.FhirDatastoreCreatedAt> CreatedAt { get; private set; } = null!;

        [Output("datastoreArn")]
        public Output<string> DatastoreArn { get; private set; } = null!;

        [Output("datastoreEndpoint")]
        public Output<string> DatastoreEndpoint { get; private set; } = null!;

        [Output("datastoreId")]
        public Output<string> DatastoreId { get; private set; } = null!;

        [Output("datastoreName")]
        public Output<string?> DatastoreName { get; private set; } = null!;

        [Output("datastoreStatus")]
        public Output<Pulumi.AwsNative.HealthLake.FhirDatastoreDatastoreStatus> DatastoreStatus { get; private set; } = null!;

        [Output("datastoreTypeVersion")]
        public Output<Pulumi.AwsNative.HealthLake.FhirDatastoreDatastoreTypeVersion> DatastoreTypeVersion { get; private set; } = null!;

        [Output("identityProviderConfiguration")]
        public Output<Outputs.FhirDatastoreIdentityProviderConfiguration?> IdentityProviderConfiguration { get; private set; } = null!;

        [Output("preloadDataConfig")]
        public Output<Outputs.FhirDatastorePreloadDataConfig?> PreloadDataConfig { get; private set; } = null!;

        [Output("sseConfiguration")]
        public Output<Outputs.FhirDatastoreSseConfiguration?> SseConfiguration { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.FhirDatastoreTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a FhirDatastore resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public FhirDatastore(string name, FhirDatastoreArgs args, CustomResourceOptions? options = null)
            : base("aws-native:healthlake:FhirDatastore", name, args ?? new FhirDatastoreArgs(), MakeResourceOptions(options, ""))
        {
        }

        private FhirDatastore(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:healthlake:FhirDatastore", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "datastoreName",
                    "datastoreTypeVersion",
                    "identityProviderConfiguration",
                    "preloadDataConfig",
                    "sseConfiguration",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing FhirDatastore resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static FhirDatastore Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new FhirDatastore(name, id, options);
        }
    }

    public sealed class FhirDatastoreArgs : global::Pulumi.ResourceArgs
    {
        [Input("datastoreName")]
        public Input<string>? DatastoreName { get; set; }

        [Input("datastoreTypeVersion", required: true)]
        public Input<Pulumi.AwsNative.HealthLake.FhirDatastoreDatastoreTypeVersion> DatastoreTypeVersion { get; set; } = null!;

        [Input("identityProviderConfiguration")]
        public Input<Inputs.FhirDatastoreIdentityProviderConfigurationArgs>? IdentityProviderConfiguration { get; set; }

        [Input("preloadDataConfig")]
        public Input<Inputs.FhirDatastorePreloadDataConfigArgs>? PreloadDataConfig { get; set; }

        [Input("sseConfiguration")]
        public Input<Inputs.FhirDatastoreSseConfigurationArgs>? SseConfiguration { get; set; }

        [Input("tags")]
        private InputList<Inputs.FhirDatastoreTagArgs>? _tags;
        public InputList<Inputs.FhirDatastoreTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.FhirDatastoreTagArgs>());
            set => _tags = value;
        }

        public FhirDatastoreArgs()
        {
        }
        public static new FhirDatastoreArgs Empty => new FhirDatastoreArgs();
    }
}
