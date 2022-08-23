// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package rds

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The AWS::RDS::DBCluster resource creates an Amazon Aurora DB cluster.
func LookupDBCluster(ctx *pulumi.Context, args *LookupDBClusterArgs, opts ...pulumi.InvokeOption) (*LookupDBClusterResult, error) {
	var rv LookupDBClusterResult
	err := ctx.Invoke("aws-native:rds:getDBCluster", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupDBClusterArgs struct {
	// The DB cluster identifier. This parameter is stored as a lowercase string.
	DBClusterIdentifier string `pulumi:"dBClusterIdentifier"`
}

type LookupDBClusterResult struct {
	// The amount of storage in gibibytes (GiB) to allocate to each DB instance in the Multi-AZ DB cluster.
	AllocatedStorage *int `pulumi:"allocatedStorage"`
	// Provides a list of the AWS Identity and Access Management (IAM) roles that are associated with the DB cluster. IAM roles that are associated with a DB cluster grant permission for the DB cluster to access other AWS services on your behalf.
	AssociatedRoles []DBClusterRole `pulumi:"associatedRoles"`
	// A value that indicates whether minor engine upgrades are applied automatically to the DB cluster during the maintenance window. By default, minor engine upgrades are applied automatically.
	AutoMinorVersionUpgrade *bool `pulumi:"autoMinorVersionUpgrade"`
	// The target backtrack window, in seconds. To disable backtracking, set this value to 0.
	BacktrackWindow *int `pulumi:"backtrackWindow"`
	// The number of days for which automated backups are retained.
	BackupRetentionPeriod *int `pulumi:"backupRetentionPeriod"`
	// A value that indicates whether to copy all tags from the DB cluster to snapshots of the DB cluster. The default is not to copy them.
	CopyTagsToSnapshot *bool `pulumi:"copyTagsToSnapshot"`
	// The compute and memory capacity of each DB instance in the Multi-AZ DB cluster, for example db.m6g.xlarge.
	DBClusterInstanceClass *string `pulumi:"dBClusterInstanceClass"`
	// The name of the DB cluster parameter group to associate with this DB cluster.
	DBClusterParameterGroupName *string `pulumi:"dBClusterParameterGroupName"`
	// A value that indicates whether the DB cluster has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is disabled.
	DeletionProtection *bool `pulumi:"deletionProtection"`
	// The list of log types that need to be enabled for exporting to CloudWatch Logs. The values in the list depend on the DB engine being used. For more information, see Publishing Database Logs to Amazon CloudWatch Logs in the Amazon Aurora User Guide.
	EnableCloudwatchLogsExports []string `pulumi:"enableCloudwatchLogsExports"`
	// A value that indicates whether to enable the HTTP endpoint for an Aurora Serverless DB cluster. By default, the HTTP endpoint is disabled.
	EnableHttpEndpoint *bool `pulumi:"enableHttpEndpoint"`
	// A value that indicates whether to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts. By default, mapping is disabled.
	EnableIAMDatabaseAuthentication *bool              `pulumi:"enableIAMDatabaseAuthentication"`
	Endpoint                        *DBClusterEndpoint `pulumi:"endpoint"`
	// The name of the database engine to be used for this DB cluster. Valid Values: aurora (for MySQL 5.6-compatible Aurora), aurora-mysql (for MySQL 5.7-compatible Aurora), and aurora-postgresql
	Engine *string `pulumi:"engine"`
	// The version number of the database engine to use.
	EngineVersion *string `pulumi:"engineVersion"`
	// If you are configuring an Aurora global database cluster and want your Aurora DB cluster to be a secondary member in the global database cluster, specify the global cluster ID of the global database cluster. To define the primary database cluster of the global cluster, use the AWS::RDS::GlobalCluster resource.
	//
	// If you aren't configuring a global database cluster, don't specify this property.
	GlobalClusterIdentifier *string `pulumi:"globalClusterIdentifier"`
	// The amount of Provisioned IOPS (input/output operations per second) to be initially allocated for each DB instance in the Multi-AZ DB cluster.
	Iops *int `pulumi:"iops"`
	// The name of the master user for the DB cluster. You must specify MasterUsername, unless you specify SnapshotIdentifier. In that case, don't specify MasterUsername.
	MasterUsername *string `pulumi:"masterUsername"`
	// The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB cluster. To turn off collecting Enhanced Monitoring metrics, specify 0. The default is 0.
	MonitoringInterval *int `pulumi:"monitoringInterval"`
	// The Amazon Resource Name (ARN) for the IAM role that permits RDS to send Enhanced Monitoring metrics to Amazon CloudWatch Logs.
	MonitoringRoleArn *string `pulumi:"monitoringRoleArn"`
	// A value that indicates whether to turn on Performance Insights for the DB cluster.
	PerformanceInsightsEnabled *bool `pulumi:"performanceInsightsEnabled"`
	// The Amazon Web Services KMS key identifier for encryption of Performance Insights data.
	PerformanceInsightsKmsKeyId *string `pulumi:"performanceInsightsKmsKeyId"`
	// The amount of time, in days, to retain Performance Insights data.
	PerformanceInsightsRetentionPeriod *int `pulumi:"performanceInsightsRetentionPeriod"`
	// The port number on which the instances in the DB cluster accept connections. Default: 3306 if engine is set as aurora or 5432 if set to aurora-postgresql.
	Port *int `pulumi:"port"`
	// The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter. The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region. To see the time blocks available, see Adjusting the Preferred DB Cluster Maintenance Window in the Amazon Aurora User Guide.
	PreferredBackupWindow *string `pulumi:"preferredBackupWindow"`
	// The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC). The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week. To see the time blocks available, see Adjusting the Preferred DB Cluster Maintenance Window in the Amazon Aurora User Guide.
	PreferredMaintenanceWindow *string                `pulumi:"preferredMaintenanceWindow"`
	ReadEndpoint               *DBClusterReadEndpoint `pulumi:"readEndpoint"`
	// The Amazon Resource Name (ARN) of the source DB instance or DB cluster if this DB cluster is created as a Read Replica.
	ReplicationSourceIdentifier *string `pulumi:"replicationSourceIdentifier"`
	// The ScalingConfiguration property type specifies the scaling configuration of an Aurora Serverless DB cluster.
	ScalingConfiguration *DBClusterScalingConfiguration `pulumi:"scalingConfiguration"`
	// Specifies the storage type to be associated with the DB cluster.
	StorageType *string `pulumi:"storageType"`
	// An array of key-value pairs to apply to this resource.
	Tags []DBClusterTag `pulumi:"tags"`
	// A list of EC2 VPC security groups to associate with this DB cluster.
	VpcSecurityGroupIds []string `pulumi:"vpcSecurityGroupIds"`
}

func LookupDBClusterOutput(ctx *pulumi.Context, args LookupDBClusterOutputArgs, opts ...pulumi.InvokeOption) LookupDBClusterResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupDBClusterResult, error) {
			args := v.(LookupDBClusterArgs)
			r, err := LookupDBCluster(ctx, &args, opts...)
			var s LookupDBClusterResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupDBClusterResultOutput)
}

type LookupDBClusterOutputArgs struct {
	// The DB cluster identifier. This parameter is stored as a lowercase string.
	DBClusterIdentifier pulumi.StringInput `pulumi:"dBClusterIdentifier"`
}

func (LookupDBClusterOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDBClusterArgs)(nil)).Elem()
}

type LookupDBClusterResultOutput struct{ *pulumi.OutputState }

func (LookupDBClusterResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDBClusterResult)(nil)).Elem()
}

func (o LookupDBClusterResultOutput) ToLookupDBClusterResultOutput() LookupDBClusterResultOutput {
	return o
}

func (o LookupDBClusterResultOutput) ToLookupDBClusterResultOutputWithContext(ctx context.Context) LookupDBClusterResultOutput {
	return o
}

// The amount of storage in gibibytes (GiB) to allocate to each DB instance in the Multi-AZ DB cluster.
func (o LookupDBClusterResultOutput) AllocatedStorage() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupDBClusterResult) *int { return v.AllocatedStorage }).(pulumi.IntPtrOutput)
}

// Provides a list of the AWS Identity and Access Management (IAM) roles that are associated with the DB cluster. IAM roles that are associated with a DB cluster grant permission for the DB cluster to access other AWS services on your behalf.
func (o LookupDBClusterResultOutput) AssociatedRoles() DBClusterRoleArrayOutput {
	return o.ApplyT(func(v LookupDBClusterResult) []DBClusterRole { return v.AssociatedRoles }).(DBClusterRoleArrayOutput)
}

// A value that indicates whether minor engine upgrades are applied automatically to the DB cluster during the maintenance window. By default, minor engine upgrades are applied automatically.
func (o LookupDBClusterResultOutput) AutoMinorVersionUpgrade() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupDBClusterResult) *bool { return v.AutoMinorVersionUpgrade }).(pulumi.BoolPtrOutput)
}

// The target backtrack window, in seconds. To disable backtracking, set this value to 0.
func (o LookupDBClusterResultOutput) BacktrackWindow() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupDBClusterResult) *int { return v.BacktrackWindow }).(pulumi.IntPtrOutput)
}

// The number of days for which automated backups are retained.
func (o LookupDBClusterResultOutput) BackupRetentionPeriod() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupDBClusterResult) *int { return v.BackupRetentionPeriod }).(pulumi.IntPtrOutput)
}

// A value that indicates whether to copy all tags from the DB cluster to snapshots of the DB cluster. The default is not to copy them.
func (o LookupDBClusterResultOutput) CopyTagsToSnapshot() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupDBClusterResult) *bool { return v.CopyTagsToSnapshot }).(pulumi.BoolPtrOutput)
}

// The compute and memory capacity of each DB instance in the Multi-AZ DB cluster, for example db.m6g.xlarge.
func (o LookupDBClusterResultOutput) DBClusterInstanceClass() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDBClusterResult) *string { return v.DBClusterInstanceClass }).(pulumi.StringPtrOutput)
}

// The name of the DB cluster parameter group to associate with this DB cluster.
func (o LookupDBClusterResultOutput) DBClusterParameterGroupName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDBClusterResult) *string { return v.DBClusterParameterGroupName }).(pulumi.StringPtrOutput)
}

// A value that indicates whether the DB cluster has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is disabled.
func (o LookupDBClusterResultOutput) DeletionProtection() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupDBClusterResult) *bool { return v.DeletionProtection }).(pulumi.BoolPtrOutput)
}

// The list of log types that need to be enabled for exporting to CloudWatch Logs. The values in the list depend on the DB engine being used. For more information, see Publishing Database Logs to Amazon CloudWatch Logs in the Amazon Aurora User Guide.
func (o LookupDBClusterResultOutput) EnableCloudwatchLogsExports() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupDBClusterResult) []string { return v.EnableCloudwatchLogsExports }).(pulumi.StringArrayOutput)
}

// A value that indicates whether to enable the HTTP endpoint for an Aurora Serverless DB cluster. By default, the HTTP endpoint is disabled.
func (o LookupDBClusterResultOutput) EnableHttpEndpoint() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupDBClusterResult) *bool { return v.EnableHttpEndpoint }).(pulumi.BoolPtrOutput)
}

// A value that indicates whether to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts. By default, mapping is disabled.
func (o LookupDBClusterResultOutput) EnableIAMDatabaseAuthentication() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupDBClusterResult) *bool { return v.EnableIAMDatabaseAuthentication }).(pulumi.BoolPtrOutput)
}

func (o LookupDBClusterResultOutput) Endpoint() DBClusterEndpointPtrOutput {
	return o.ApplyT(func(v LookupDBClusterResult) *DBClusterEndpoint { return v.Endpoint }).(DBClusterEndpointPtrOutput)
}

// The name of the database engine to be used for this DB cluster. Valid Values: aurora (for MySQL 5.6-compatible Aurora), aurora-mysql (for MySQL 5.7-compatible Aurora), and aurora-postgresql
func (o LookupDBClusterResultOutput) Engine() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDBClusterResult) *string { return v.Engine }).(pulumi.StringPtrOutput)
}

// The version number of the database engine to use.
func (o LookupDBClusterResultOutput) EngineVersion() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDBClusterResult) *string { return v.EngineVersion }).(pulumi.StringPtrOutput)
}

// If you are configuring an Aurora global database cluster and want your Aurora DB cluster to be a secondary member in the global database cluster, specify the global cluster ID of the global database cluster. To define the primary database cluster of the global cluster, use the AWS::RDS::GlobalCluster resource.
//
// If you aren't configuring a global database cluster, don't specify this property.
func (o LookupDBClusterResultOutput) GlobalClusterIdentifier() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDBClusterResult) *string { return v.GlobalClusterIdentifier }).(pulumi.StringPtrOutput)
}

// The amount of Provisioned IOPS (input/output operations per second) to be initially allocated for each DB instance in the Multi-AZ DB cluster.
func (o LookupDBClusterResultOutput) Iops() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupDBClusterResult) *int { return v.Iops }).(pulumi.IntPtrOutput)
}

// The name of the master user for the DB cluster. You must specify MasterUsername, unless you specify SnapshotIdentifier. In that case, don't specify MasterUsername.
func (o LookupDBClusterResultOutput) MasterUsername() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDBClusterResult) *string { return v.MasterUsername }).(pulumi.StringPtrOutput)
}

// The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB cluster. To turn off collecting Enhanced Monitoring metrics, specify 0. The default is 0.
func (o LookupDBClusterResultOutput) MonitoringInterval() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupDBClusterResult) *int { return v.MonitoringInterval }).(pulumi.IntPtrOutput)
}

// The Amazon Resource Name (ARN) for the IAM role that permits RDS to send Enhanced Monitoring metrics to Amazon CloudWatch Logs.
func (o LookupDBClusterResultOutput) MonitoringRoleArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDBClusterResult) *string { return v.MonitoringRoleArn }).(pulumi.StringPtrOutput)
}

// A value that indicates whether to turn on Performance Insights for the DB cluster.
func (o LookupDBClusterResultOutput) PerformanceInsightsEnabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupDBClusterResult) *bool { return v.PerformanceInsightsEnabled }).(pulumi.BoolPtrOutput)
}

// The Amazon Web Services KMS key identifier for encryption of Performance Insights data.
func (o LookupDBClusterResultOutput) PerformanceInsightsKmsKeyId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDBClusterResult) *string { return v.PerformanceInsightsKmsKeyId }).(pulumi.StringPtrOutput)
}

// The amount of time, in days, to retain Performance Insights data.
func (o LookupDBClusterResultOutput) PerformanceInsightsRetentionPeriod() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupDBClusterResult) *int { return v.PerformanceInsightsRetentionPeriod }).(pulumi.IntPtrOutput)
}

// The port number on which the instances in the DB cluster accept connections. Default: 3306 if engine is set as aurora or 5432 if set to aurora-postgresql.
func (o LookupDBClusterResultOutput) Port() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupDBClusterResult) *int { return v.Port }).(pulumi.IntPtrOutput)
}

// The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter. The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region. To see the time blocks available, see Adjusting the Preferred DB Cluster Maintenance Window in the Amazon Aurora User Guide.
func (o LookupDBClusterResultOutput) PreferredBackupWindow() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDBClusterResult) *string { return v.PreferredBackupWindow }).(pulumi.StringPtrOutput)
}

// The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC). The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week. To see the time blocks available, see Adjusting the Preferred DB Cluster Maintenance Window in the Amazon Aurora User Guide.
func (o LookupDBClusterResultOutput) PreferredMaintenanceWindow() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDBClusterResult) *string { return v.PreferredMaintenanceWindow }).(pulumi.StringPtrOutput)
}

func (o LookupDBClusterResultOutput) ReadEndpoint() DBClusterReadEndpointPtrOutput {
	return o.ApplyT(func(v LookupDBClusterResult) *DBClusterReadEndpoint { return v.ReadEndpoint }).(DBClusterReadEndpointPtrOutput)
}

// The Amazon Resource Name (ARN) of the source DB instance or DB cluster if this DB cluster is created as a Read Replica.
func (o LookupDBClusterResultOutput) ReplicationSourceIdentifier() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDBClusterResult) *string { return v.ReplicationSourceIdentifier }).(pulumi.StringPtrOutput)
}

// The ScalingConfiguration property type specifies the scaling configuration of an Aurora Serverless DB cluster.
func (o LookupDBClusterResultOutput) ScalingConfiguration() DBClusterScalingConfigurationPtrOutput {
	return o.ApplyT(func(v LookupDBClusterResult) *DBClusterScalingConfiguration { return v.ScalingConfiguration }).(DBClusterScalingConfigurationPtrOutput)
}

// Specifies the storage type to be associated with the DB cluster.
func (o LookupDBClusterResultOutput) StorageType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDBClusterResult) *string { return v.StorageType }).(pulumi.StringPtrOutput)
}

// An array of key-value pairs to apply to this resource.
func (o LookupDBClusterResultOutput) Tags() DBClusterTagArrayOutput {
	return o.ApplyT(func(v LookupDBClusterResult) []DBClusterTag { return v.Tags }).(DBClusterTagArrayOutput)
}

// A list of EC2 VPC security groups to associate with this DB cluster.
func (o LookupDBClusterResultOutput) VpcSecurityGroupIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupDBClusterResult) []string { return v.VpcSecurityGroupIds }).(pulumi.StringArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupDBClusterResultOutput{})
}
