// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package docdb

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::DocDB::DBCluster
//
// Deprecated: DBCluster is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type DBCluster struct {
	pulumi.CustomResourceState

	AvailabilityZones           pulumi.StringArrayOutput `pulumi:"availabilityZones"`
	BackupRetentionPeriod       pulumi.IntPtrOutput      `pulumi:"backupRetentionPeriod"`
	ClusterResourceId           pulumi.StringOutput      `pulumi:"clusterResourceId"`
	CopyTagsToSnapshot          pulumi.BoolPtrOutput     `pulumi:"copyTagsToSnapshot"`
	DbClusterIdentifier         pulumi.StringPtrOutput   `pulumi:"dbClusterIdentifier"`
	DbClusterParameterGroupName pulumi.StringPtrOutput   `pulumi:"dbClusterParameterGroupName"`
	DbSubnetGroupName           pulumi.StringPtrOutput   `pulumi:"dbSubnetGroupName"`
	DeletionProtection          pulumi.BoolPtrOutput     `pulumi:"deletionProtection"`
	EnableCloudwatchLogsExports pulumi.StringArrayOutput `pulumi:"enableCloudwatchLogsExports"`
	Endpoint                    pulumi.StringOutput      `pulumi:"endpoint"`
	EngineVersion               pulumi.StringPtrOutput   `pulumi:"engineVersion"`
	KmsKeyId                    pulumi.StringPtrOutput   `pulumi:"kmsKeyId"`
	MasterUserPassword          pulumi.StringPtrOutput   `pulumi:"masterUserPassword"`
	MasterUsername              pulumi.StringPtrOutput   `pulumi:"masterUsername"`
	Port                        pulumi.IntPtrOutput      `pulumi:"port"`
	PreferredBackupWindow       pulumi.StringPtrOutput   `pulumi:"preferredBackupWindow"`
	PreferredMaintenanceWindow  pulumi.StringPtrOutput   `pulumi:"preferredMaintenanceWindow"`
	ReadEndpoint                pulumi.StringOutput      `pulumi:"readEndpoint"`
	RestoreToTime               pulumi.StringPtrOutput   `pulumi:"restoreToTime"`
	RestoreType                 pulumi.StringPtrOutput   `pulumi:"restoreType"`
	SnapshotIdentifier          pulumi.StringPtrOutput   `pulumi:"snapshotIdentifier"`
	SourceDbClusterIdentifier   pulumi.StringPtrOutput   `pulumi:"sourceDbClusterIdentifier"`
	StorageEncrypted            pulumi.BoolPtrOutput     `pulumi:"storageEncrypted"`
	Tags                        DBClusterTagArrayOutput  `pulumi:"tags"`
	UseLatestRestorableTime     pulumi.BoolPtrOutput     `pulumi:"useLatestRestorableTime"`
	VpcSecurityGroupIds         pulumi.StringArrayOutput `pulumi:"vpcSecurityGroupIds"`
}

// NewDBCluster registers a new resource with the given unique name, arguments, and options.
func NewDBCluster(ctx *pulumi.Context,
	name string, args *DBClusterArgs, opts ...pulumi.ResourceOption) (*DBCluster, error) {
	if args == nil {
		args = &DBClusterArgs{}
	}

	opts = internal.PkgResourceDefaultOpts(opts)
	var resource DBCluster
	err := ctx.RegisterResource("aws-native:docdb:DBCluster", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDBCluster gets an existing DBCluster resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDBCluster(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DBClusterState, opts ...pulumi.ResourceOption) (*DBCluster, error) {
	var resource DBCluster
	err := ctx.ReadResource("aws-native:docdb:DBCluster", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DBCluster resources.
type dbclusterState struct {
}

type DBClusterState struct {
}

func (DBClusterState) ElementType() reflect.Type {
	return reflect.TypeOf((*dbclusterState)(nil)).Elem()
}

type dbclusterArgs struct {
	AvailabilityZones           []string       `pulumi:"availabilityZones"`
	BackupRetentionPeriod       *int           `pulumi:"backupRetentionPeriod"`
	CopyTagsToSnapshot          *bool          `pulumi:"copyTagsToSnapshot"`
	DbClusterIdentifier         *string        `pulumi:"dbClusterIdentifier"`
	DbClusterParameterGroupName *string        `pulumi:"dbClusterParameterGroupName"`
	DbSubnetGroupName           *string        `pulumi:"dbSubnetGroupName"`
	DeletionProtection          *bool          `pulumi:"deletionProtection"`
	EnableCloudwatchLogsExports []string       `pulumi:"enableCloudwatchLogsExports"`
	EngineVersion               *string        `pulumi:"engineVersion"`
	KmsKeyId                    *string        `pulumi:"kmsKeyId"`
	MasterUserPassword          *string        `pulumi:"masterUserPassword"`
	MasterUsername              *string        `pulumi:"masterUsername"`
	Port                        *int           `pulumi:"port"`
	PreferredBackupWindow       *string        `pulumi:"preferredBackupWindow"`
	PreferredMaintenanceWindow  *string        `pulumi:"preferredMaintenanceWindow"`
	RestoreToTime               *string        `pulumi:"restoreToTime"`
	RestoreType                 *string        `pulumi:"restoreType"`
	SnapshotIdentifier          *string        `pulumi:"snapshotIdentifier"`
	SourceDbClusterIdentifier   *string        `pulumi:"sourceDbClusterIdentifier"`
	StorageEncrypted            *bool          `pulumi:"storageEncrypted"`
	Tags                        []DBClusterTag `pulumi:"tags"`
	UseLatestRestorableTime     *bool          `pulumi:"useLatestRestorableTime"`
	VpcSecurityGroupIds         []string       `pulumi:"vpcSecurityGroupIds"`
}

// The set of arguments for constructing a DBCluster resource.
type DBClusterArgs struct {
	AvailabilityZones           pulumi.StringArrayInput
	BackupRetentionPeriod       pulumi.IntPtrInput
	CopyTagsToSnapshot          pulumi.BoolPtrInput
	DbClusterIdentifier         pulumi.StringPtrInput
	DbClusterParameterGroupName pulumi.StringPtrInput
	DbSubnetGroupName           pulumi.StringPtrInput
	DeletionProtection          pulumi.BoolPtrInput
	EnableCloudwatchLogsExports pulumi.StringArrayInput
	EngineVersion               pulumi.StringPtrInput
	KmsKeyId                    pulumi.StringPtrInput
	MasterUserPassword          pulumi.StringPtrInput
	MasterUsername              pulumi.StringPtrInput
	Port                        pulumi.IntPtrInput
	PreferredBackupWindow       pulumi.StringPtrInput
	PreferredMaintenanceWindow  pulumi.StringPtrInput
	RestoreToTime               pulumi.StringPtrInput
	RestoreType                 pulumi.StringPtrInput
	SnapshotIdentifier          pulumi.StringPtrInput
	SourceDbClusterIdentifier   pulumi.StringPtrInput
	StorageEncrypted            pulumi.BoolPtrInput
	Tags                        DBClusterTagArrayInput
	UseLatestRestorableTime     pulumi.BoolPtrInput
	VpcSecurityGroupIds         pulumi.StringArrayInput
}

func (DBClusterArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*dbclusterArgs)(nil)).Elem()
}

type DBClusterInput interface {
	pulumi.Input

	ToDBClusterOutput() DBClusterOutput
	ToDBClusterOutputWithContext(ctx context.Context) DBClusterOutput
}

func (*DBCluster) ElementType() reflect.Type {
	return reflect.TypeOf((**DBCluster)(nil)).Elem()
}

func (i *DBCluster) ToDBClusterOutput() DBClusterOutput {
	return i.ToDBClusterOutputWithContext(context.Background())
}

func (i *DBCluster) ToDBClusterOutputWithContext(ctx context.Context) DBClusterOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DBClusterOutput)
}

type DBClusterOutput struct{ *pulumi.OutputState }

func (DBClusterOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DBCluster)(nil)).Elem()
}

func (o DBClusterOutput) ToDBClusterOutput() DBClusterOutput {
	return o
}

func (o DBClusterOutput) ToDBClusterOutputWithContext(ctx context.Context) DBClusterOutput {
	return o
}

func (o DBClusterOutput) AvailabilityZones() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *DBCluster) pulumi.StringArrayOutput { return v.AvailabilityZones }).(pulumi.StringArrayOutput)
}

func (o DBClusterOutput) BackupRetentionPeriod() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *DBCluster) pulumi.IntPtrOutput { return v.BackupRetentionPeriod }).(pulumi.IntPtrOutput)
}

func (o DBClusterOutput) ClusterResourceId() pulumi.StringOutput {
	return o.ApplyT(func(v *DBCluster) pulumi.StringOutput { return v.ClusterResourceId }).(pulumi.StringOutput)
}

func (o DBClusterOutput) CopyTagsToSnapshot() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *DBCluster) pulumi.BoolPtrOutput { return v.CopyTagsToSnapshot }).(pulumi.BoolPtrOutput)
}

func (o DBClusterOutput) DbClusterIdentifier() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DBCluster) pulumi.StringPtrOutput { return v.DbClusterIdentifier }).(pulumi.StringPtrOutput)
}

func (o DBClusterOutput) DbClusterParameterGroupName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DBCluster) pulumi.StringPtrOutput { return v.DbClusterParameterGroupName }).(pulumi.StringPtrOutput)
}

func (o DBClusterOutput) DbSubnetGroupName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DBCluster) pulumi.StringPtrOutput { return v.DbSubnetGroupName }).(pulumi.StringPtrOutput)
}

func (o DBClusterOutput) DeletionProtection() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *DBCluster) pulumi.BoolPtrOutput { return v.DeletionProtection }).(pulumi.BoolPtrOutput)
}

func (o DBClusterOutput) EnableCloudwatchLogsExports() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *DBCluster) pulumi.StringArrayOutput { return v.EnableCloudwatchLogsExports }).(pulumi.StringArrayOutput)
}

func (o DBClusterOutput) Endpoint() pulumi.StringOutput {
	return o.ApplyT(func(v *DBCluster) pulumi.StringOutput { return v.Endpoint }).(pulumi.StringOutput)
}

func (o DBClusterOutput) EngineVersion() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DBCluster) pulumi.StringPtrOutput { return v.EngineVersion }).(pulumi.StringPtrOutput)
}

func (o DBClusterOutput) KmsKeyId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DBCluster) pulumi.StringPtrOutput { return v.KmsKeyId }).(pulumi.StringPtrOutput)
}

func (o DBClusterOutput) MasterUserPassword() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DBCluster) pulumi.StringPtrOutput { return v.MasterUserPassword }).(pulumi.StringPtrOutput)
}

func (o DBClusterOutput) MasterUsername() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DBCluster) pulumi.StringPtrOutput { return v.MasterUsername }).(pulumi.StringPtrOutput)
}

func (o DBClusterOutput) Port() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *DBCluster) pulumi.IntPtrOutput { return v.Port }).(pulumi.IntPtrOutput)
}

func (o DBClusterOutput) PreferredBackupWindow() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DBCluster) pulumi.StringPtrOutput { return v.PreferredBackupWindow }).(pulumi.StringPtrOutput)
}

func (o DBClusterOutput) PreferredMaintenanceWindow() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DBCluster) pulumi.StringPtrOutput { return v.PreferredMaintenanceWindow }).(pulumi.StringPtrOutput)
}

func (o DBClusterOutput) ReadEndpoint() pulumi.StringOutput {
	return o.ApplyT(func(v *DBCluster) pulumi.StringOutput { return v.ReadEndpoint }).(pulumi.StringOutput)
}

func (o DBClusterOutput) RestoreToTime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DBCluster) pulumi.StringPtrOutput { return v.RestoreToTime }).(pulumi.StringPtrOutput)
}

func (o DBClusterOutput) RestoreType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DBCluster) pulumi.StringPtrOutput { return v.RestoreType }).(pulumi.StringPtrOutput)
}

func (o DBClusterOutput) SnapshotIdentifier() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DBCluster) pulumi.StringPtrOutput { return v.SnapshotIdentifier }).(pulumi.StringPtrOutput)
}

func (o DBClusterOutput) SourceDbClusterIdentifier() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DBCluster) pulumi.StringPtrOutput { return v.SourceDbClusterIdentifier }).(pulumi.StringPtrOutput)
}

func (o DBClusterOutput) StorageEncrypted() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *DBCluster) pulumi.BoolPtrOutput { return v.StorageEncrypted }).(pulumi.BoolPtrOutput)
}

func (o DBClusterOutput) Tags() DBClusterTagArrayOutput {
	return o.ApplyT(func(v *DBCluster) DBClusterTagArrayOutput { return v.Tags }).(DBClusterTagArrayOutput)
}

func (o DBClusterOutput) UseLatestRestorableTime() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *DBCluster) pulumi.BoolPtrOutput { return v.UseLatestRestorableTime }).(pulumi.BoolPtrOutput)
}

func (o DBClusterOutput) VpcSecurityGroupIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *DBCluster) pulumi.StringArrayOutput { return v.VpcSecurityGroupIds }).(pulumi.StringArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DBClusterInput)(nil)).Elem(), &DBCluster{})
	pulumi.RegisterOutputType(DBClusterOutput{})
}
