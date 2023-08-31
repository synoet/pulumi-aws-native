// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.RedshiftServerless
{
    /// <summary>
    /// Definition of AWS::RedshiftServerless::Workgroup Resource Type
    /// </summary>
    [AwsNativeResourceType("aws-native:redshiftserverless:Workgroup")]
    public partial class Workgroup : global::Pulumi.CustomResource
    {
        [Output("baseCapacity")]
        public Output<int?> BaseCapacity { get; private set; } = null!;

        [Output("configParameters")]
        public Output<ImmutableArray<Outputs.WorkgroupConfigParameter>> ConfigParameters { get; private set; } = null!;

        [Output("enhancedVpcRouting")]
        public Output<bool?> EnhancedVpcRouting { get; private set; } = null!;

        [Output("namespaceName")]
        public Output<string?> NamespaceName { get; private set; } = null!;

        [Output("port")]
        public Output<int?> Port { get; private set; } = null!;

        [Output("publiclyAccessible")]
        public Output<bool?> PubliclyAccessible { get; private set; } = null!;

        [Output("securityGroupIds")]
        public Output<ImmutableArray<string>> SecurityGroupIds { get; private set; } = null!;

        [Output("subnetIds")]
        public Output<ImmutableArray<string>> SubnetIds { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.WorkgroupTag>> Tags { get; private set; } = null!;

        [Output("workgroup")]
        public Output<Outputs.Workgroup> WorkgroupValue { get; private set; } = null!;

        [Output("workgroupName")]
        public Output<string> WorkgroupName { get; private set; } = null!;


        /// <summary>
        /// Create a Workgroup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Workgroup(string name, WorkgroupArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:redshiftserverless:Workgroup", name, args ?? new WorkgroupArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Workgroup(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:redshiftserverless:Workgroup", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "namespaceName",
                    "workgroupName",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Workgroup resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Workgroup Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Workgroup(name, id, options);
        }
    }

    public sealed class WorkgroupArgs : global::Pulumi.ResourceArgs
    {
        [Input("baseCapacity")]
        public Input<int>? BaseCapacity { get; set; }

        [Input("configParameters")]
        private InputList<Inputs.WorkgroupConfigParameterArgs>? _configParameters;
        public InputList<Inputs.WorkgroupConfigParameterArgs> ConfigParameters
        {
            get => _configParameters ?? (_configParameters = new InputList<Inputs.WorkgroupConfigParameterArgs>());
            set => _configParameters = value;
        }

        [Input("enhancedVpcRouting")]
        public Input<bool>? EnhancedVpcRouting { get; set; }

        [Input("namespaceName")]
        public Input<string>? NamespaceName { get; set; }

        [Input("port")]
        public Input<int>? Port { get; set; }

        [Input("publiclyAccessible")]
        public Input<bool>? PubliclyAccessible { get; set; }

        [Input("securityGroupIds")]
        private InputList<string>? _securityGroupIds;
        public InputList<string> SecurityGroupIds
        {
            get => _securityGroupIds ?? (_securityGroupIds = new InputList<string>());
            set => _securityGroupIds = value;
        }

        [Input("subnetIds")]
        private InputList<string>? _subnetIds;
        public InputList<string> SubnetIds
        {
            get => _subnetIds ?? (_subnetIds = new InputList<string>());
            set => _subnetIds = value;
        }

        [Input("tags")]
        private InputList<Inputs.WorkgroupTagArgs>? _tags;
        public InputList<Inputs.WorkgroupTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.WorkgroupTagArgs>());
            set => _tags = value;
        }

        [Input("workgroupName")]
        public Input<string>? WorkgroupName { get; set; }

        public WorkgroupArgs()
        {
        }
        public static new WorkgroupArgs Empty => new WorkgroupArgs();
    }
}
