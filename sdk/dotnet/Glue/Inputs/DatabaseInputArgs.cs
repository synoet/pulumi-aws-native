// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Glue.Inputs
{

    public sealed class DatabaseInputArgs : global::Pulumi.ResourceArgs
    {
        [Input("createTableDefaultPermissions")]
        private InputList<Inputs.DatabasePrincipalPrivilegesArgs>? _createTableDefaultPermissions;
        public InputList<Inputs.DatabasePrincipalPrivilegesArgs> CreateTableDefaultPermissions
        {
            get => _createTableDefaultPermissions ?? (_createTableDefaultPermissions = new InputList<Inputs.DatabasePrincipalPrivilegesArgs>());
            set => _createTableDefaultPermissions = value;
        }

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("federatedDatabase")]
        public Input<Inputs.DatabaseFederatedDatabaseArgs>? FederatedDatabase { get; set; }

        [Input("locationUri")]
        public Input<string>? LocationUri { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("parameters")]
        public Input<object>? Parameters { get; set; }

        [Input("targetDatabase")]
        public Input<Inputs.DatabaseIdentifierArgs>? TargetDatabase { get; set; }

        public DatabaseInputArgs()
        {
        }
        public static new DatabaseInputArgs Empty => new DatabaseInputArgs();
    }
}
