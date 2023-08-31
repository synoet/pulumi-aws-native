// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Lightsail
{
    /// <summary>
    /// Resource Type definition for AWS::Lightsail::Database
    /// </summary>
    [AwsNativeResourceType("aws-native:lightsail:Database")]
    public partial class Database : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The Availability Zone in which to create your new database. Use the us-east-2a case-sensitive format.
        /// </summary>
        [Output("availabilityZone")]
        public Output<string?> AvailabilityZone { get; private set; } = null!;

        /// <summary>
        /// When true, enables automated backup retention for your database. Updates are applied during the next maintenance window because this can result in an outage.
        /// </summary>
        [Output("backupRetention")]
        public Output<bool?> BackupRetention { get; private set; } = null!;

        /// <summary>
        /// Indicates the certificate that needs to be associated with the database.
        /// </summary>
        [Output("caCertificateIdentifier")]
        public Output<string?> CaCertificateIdentifier { get; private set; } = null!;

        [Output("databaseArn")]
        public Output<string> DatabaseArn { get; private set; } = null!;

        /// <summary>
        /// The name of the database to create when the Lightsail database resource is created. For MySQL, if this parameter isn't specified, no database is created in the database resource. For PostgreSQL, if this parameter isn't specified, a database named postgres is created in the database resource.
        /// </summary>
        [Output("masterDatabaseName")]
        public Output<string> MasterDatabaseName { get; private set; } = null!;

        /// <summary>
        /// The password for the master user. The password can include any printable ASCII character except "/", """, or "@". It cannot contain spaces.
        /// </summary>
        [Output("masterUserPassword")]
        public Output<string?> MasterUserPassword { get; private set; } = null!;

        /// <summary>
        /// The name for the master user.
        /// </summary>
        [Output("masterUsername")]
        public Output<string> MasterUsername { get; private set; } = null!;

        /// <summary>
        /// The daily time range during which automated backups are created for your new database if automated backups are enabled.
        /// </summary>
        [Output("preferredBackupWindow")]
        public Output<string?> PreferredBackupWindow { get; private set; } = null!;

        /// <summary>
        /// The weekly time range during which system maintenance can occur on your new database.
        /// </summary>
        [Output("preferredMaintenanceWindow")]
        public Output<string?> PreferredMaintenanceWindow { get; private set; } = null!;

        /// <summary>
        /// Specifies the accessibility options for your new database. A value of true specifies a database that is available to resources outside of your Lightsail account. A value of false specifies a database that is available only to your Lightsail resources in the same region as your database.
        /// </summary>
        [Output("publiclyAccessible")]
        public Output<bool?> PubliclyAccessible { get; private set; } = null!;

        /// <summary>
        /// The blueprint ID for your new database. A blueprint describes the major engine version of a database.
        /// </summary>
        [Output("relationalDatabaseBlueprintId")]
        public Output<string> RelationalDatabaseBlueprintId { get; private set; } = null!;

        /// <summary>
        /// The bundle ID for your new database. A bundle describes the performance specifications for your database.
        /// </summary>
        [Output("relationalDatabaseBundleId")]
        public Output<string> RelationalDatabaseBundleId { get; private set; } = null!;

        /// <summary>
        /// The name to use for your new Lightsail database resource.
        /// </summary>
        [Output("relationalDatabaseName")]
        public Output<string> RelationalDatabaseName { get; private set; } = null!;

        /// <summary>
        /// Update one or more parameters of the relational database.
        /// </summary>
        [Output("relationalDatabaseParameters")]
        public Output<ImmutableArray<Outputs.DatabaseRelationalDatabaseParameter>> RelationalDatabaseParameters { get; private set; } = null!;

        /// <summary>
        /// When true, the master user password is changed to a new strong password generated by Lightsail. Use the get relational database master user password operation to get the new password.
        /// </summary>
        [Output("rotateMasterUserPassword")]
        public Output<bool?> RotateMasterUserPassword { get; private set; } = null!;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.DatabaseTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Database resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Database(string name, DatabaseArgs args, CustomResourceOptions? options = null)
            : base("aws-native:lightsail:Database", name, args ?? new DatabaseArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Database(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:lightsail:Database", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "availabilityZone",
                    "masterDatabaseName",
                    "masterUsername",
                    "relationalDatabaseBlueprintId",
                    "relationalDatabaseBundleId",
                    "relationalDatabaseName",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Database resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Database Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Database(name, id, options);
        }
    }

    public sealed class DatabaseArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Availability Zone in which to create your new database. Use the us-east-2a case-sensitive format.
        /// </summary>
        [Input("availabilityZone")]
        public Input<string>? AvailabilityZone { get; set; }

        /// <summary>
        /// When true, enables automated backup retention for your database. Updates are applied during the next maintenance window because this can result in an outage.
        /// </summary>
        [Input("backupRetention")]
        public Input<bool>? BackupRetention { get; set; }

        /// <summary>
        /// Indicates the certificate that needs to be associated with the database.
        /// </summary>
        [Input("caCertificateIdentifier")]
        public Input<string>? CaCertificateIdentifier { get; set; }

        /// <summary>
        /// The name of the database to create when the Lightsail database resource is created. For MySQL, if this parameter isn't specified, no database is created in the database resource. For PostgreSQL, if this parameter isn't specified, a database named postgres is created in the database resource.
        /// </summary>
        [Input("masterDatabaseName", required: true)]
        public Input<string> MasterDatabaseName { get; set; } = null!;

        /// <summary>
        /// The password for the master user. The password can include any printable ASCII character except "/", """, or "@". It cannot contain spaces.
        /// </summary>
        [Input("masterUserPassword")]
        public Input<string>? MasterUserPassword { get; set; }

        /// <summary>
        /// The name for the master user.
        /// </summary>
        [Input("masterUsername", required: true)]
        public Input<string> MasterUsername { get; set; } = null!;

        /// <summary>
        /// The daily time range during which automated backups are created for your new database if automated backups are enabled.
        /// </summary>
        [Input("preferredBackupWindow")]
        public Input<string>? PreferredBackupWindow { get; set; }

        /// <summary>
        /// The weekly time range during which system maintenance can occur on your new database.
        /// </summary>
        [Input("preferredMaintenanceWindow")]
        public Input<string>? PreferredMaintenanceWindow { get; set; }

        /// <summary>
        /// Specifies the accessibility options for your new database. A value of true specifies a database that is available to resources outside of your Lightsail account. A value of false specifies a database that is available only to your Lightsail resources in the same region as your database.
        /// </summary>
        [Input("publiclyAccessible")]
        public Input<bool>? PubliclyAccessible { get; set; }

        /// <summary>
        /// The blueprint ID for your new database. A blueprint describes the major engine version of a database.
        /// </summary>
        [Input("relationalDatabaseBlueprintId", required: true)]
        public Input<string> RelationalDatabaseBlueprintId { get; set; } = null!;

        /// <summary>
        /// The bundle ID for your new database. A bundle describes the performance specifications for your database.
        /// </summary>
        [Input("relationalDatabaseBundleId", required: true)]
        public Input<string> RelationalDatabaseBundleId { get; set; } = null!;

        /// <summary>
        /// The name to use for your new Lightsail database resource.
        /// </summary>
        [Input("relationalDatabaseName", required: true)]
        public Input<string> RelationalDatabaseName { get; set; } = null!;

        [Input("relationalDatabaseParameters")]
        private InputList<Inputs.DatabaseRelationalDatabaseParameterArgs>? _relationalDatabaseParameters;

        /// <summary>
        /// Update one or more parameters of the relational database.
        /// </summary>
        public InputList<Inputs.DatabaseRelationalDatabaseParameterArgs> RelationalDatabaseParameters
        {
            get => _relationalDatabaseParameters ?? (_relationalDatabaseParameters = new InputList<Inputs.DatabaseRelationalDatabaseParameterArgs>());
            set => _relationalDatabaseParameters = value;
        }

        /// <summary>
        /// When true, the master user password is changed to a new strong password generated by Lightsail. Use the get relational database master user password operation to get the new password.
        /// </summary>
        [Input("rotateMasterUserPassword")]
        public Input<bool>? RotateMasterUserPassword { get; set; }

        [Input("tags")]
        private InputList<Inputs.DatabaseTagArgs>? _tags;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public InputList<Inputs.DatabaseTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.DatabaseTagArgs>());
            set => _tags = value;
        }

        public DatabaseArgs()
        {
        }
        public static new DatabaseArgs Empty => new DatabaseArgs();
    }
}
