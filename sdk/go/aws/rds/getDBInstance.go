// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package rds

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The AWS::RDS::DBInstance resource creates an Amazon RDS DB instance.
func LookupDBInstance(ctx *pulumi.Context, args *LookupDBInstanceArgs, opts ...pulumi.InvokeOption) (*LookupDBInstanceResult, error) {
	var rv LookupDBInstanceResult
	err := ctx.Invoke("aws-native:rds:getDBInstance", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupDBInstanceArgs struct {
	// A name for the DB instance. If you specify a name, AWS CloudFormation converts it to lowercase. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the DB instance.
	DBInstanceIdentifier string `pulumi:"dBInstanceIdentifier"`
}

type LookupDBInstanceResult struct {
	// The amount of storage (in gigabytes) to be initially allocated for the database instance.
	AllocatedStorage *string `pulumi:"allocatedStorage"`
	// A value that indicates whether major version upgrades are allowed. Changing this parameter doesn't result in an outage and the change is asynchronously applied as soon as possible.
	AllowMajorVersionUpgrade *bool `pulumi:"allowMajorVersionUpgrade"`
	// The AWS Identity and Access Management (IAM) roles associated with the DB instance.
	AssociatedRoles []DBInstanceRole `pulumi:"associatedRoles"`
	// A value that indicates whether minor engine upgrades are applied automatically to the DB instance during the maintenance window. By default, minor engine upgrades are applied automatically.
	AutoMinorVersionUpgrade *bool `pulumi:"autoMinorVersionUpgrade"`
	// The Availability Zone (AZ) where the database will be created. For information on AWS Regions and Availability Zones.
	AvailabilityZone *string `pulumi:"availabilityZone"`
	// The number of days for which automated backups are retained. Setting this parameter to a positive number enables backups. Setting this parameter to 0 disables automated backups.
	BackupRetentionPeriod *int `pulumi:"backupRetentionPeriod"`
	// The identifier of the CA certificate for this DB instance.
	CACertificateIdentifier *string `pulumi:"cACertificateIdentifier"`
	// A value that indicates whether to copy tags from the DB instance to snapshots of the DB instance. By default, tags are not copied.
	CopyTagsToSnapshot *bool `pulumi:"copyTagsToSnapshot"`
	// The identifier for the RDS for MySQL Multi-AZ DB cluster snapshot to restore from. For more information on Multi-AZ DB clusters, see Multi-AZ deployments with two readable standby DB instances in the Amazon RDS User Guide .
	//
	// Constraints:
	//  * Must match the identifier of an existing Multi-AZ DB cluster snapshot.
	//  * Can't be specified when DBSnapshotIdentifier is specified.
	//  * Must be specified when DBSnapshotIdentifier isn't specified.
	//  * If you are restoring from a shared manual Multi-AZ DB cluster snapshot, the DBClusterSnapshotIdentifier must be the ARN of the shared snapshot.
	//  * Can't be the identifier of an Aurora DB cluster snapshot.
	//  * Can't be the identifier of an RDS for PostgreSQL Multi-AZ DB cluster snapshot.
	DBClusterSnapshotIdentifier *string `pulumi:"dBClusterSnapshotIdentifier"`
	// The Amazon Resource Name (ARN) for the DB instance.
	DBInstanceArn *string `pulumi:"dBInstanceArn"`
	// The compute and memory capacity of the DB instance, for example, db.m4.large. Not all DB instance classes are available in all AWS Regions, or for all database engines.
	DBInstanceClass *string `pulumi:"dBInstanceClass"`
	// The name of an existing DB parameter group or a reference to an AWS::RDS::DBParameterGroup resource created in the template.
	DBParameterGroupName *string `pulumi:"dBParameterGroupName"`
	// A list of the DB security groups to assign to the DB instance. The list can include both the name of existing DB security groups or references to AWS::RDS::DBSecurityGroup resources created in the template.
	DBSecurityGroups []string `pulumi:"dBSecurityGroups"`
	// The Oracle system ID (Oracle SID) for a container database (CDB). The Oracle SID is also the name of the CDB. This setting is valid for RDS Custom only.
	DBSystemId *string `pulumi:"dBSystemId"`
	// The AWS Region-unique, immutable identifier for the DB instance. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.
	DbiResourceId *string `pulumi:"dbiResourceId"`
	// A value that indicates whether to remove automated backups immediately after the DB instance is deleted. This parameter isn't case-sensitive. The default is to remove automated backups immediately after the DB instance is deleted.
	DeleteAutomatedBackups *bool `pulumi:"deleteAutomatedBackups"`
	// A value that indicates whether the DB instance has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is disabled.
	DeletionProtection *bool `pulumi:"deletionProtection"`
	// The Active Directory directory ID to create the DB instance in. Currently, only MySQL, Microsoft SQL Server, Oracle, and PostgreSQL DB instances can be created in an Active Directory Domain.
	Domain *string `pulumi:"domain"`
	// Specify the name of the IAM role to be used when making API calls to the Directory Service.
	DomainIAMRoleName *string `pulumi:"domainIAMRoleName"`
	// The list of log types that need to be enabled for exporting to CloudWatch Logs. The values in the list depend on the DB engine being used.
	EnableCloudwatchLogsExports []string `pulumi:"enableCloudwatchLogsExports"`
	// A value that indicates whether to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts. By default, mapping is disabled.
	EnableIAMDatabaseAuthentication *bool `pulumi:"enableIAMDatabaseAuthentication"`
	// A value that indicates whether to enable Performance Insights for the DB instance.
	EnablePerformanceInsights *bool `pulumi:"enablePerformanceInsights"`
	// Specifies the connection endpoint.
	Endpoint *DBInstanceEndpoint `pulumi:"endpoint"`
	// The name of the database engine that you want to use for this DB instance.
	Engine *string `pulumi:"engine"`
	// The version number of the database engine to use.
	EngineVersion *string `pulumi:"engineVersion"`
	// The number of I/O operations per second (IOPS) that the database provisions.
	Iops *int `pulumi:"iops"`
	// License model information for this DB instance.
	LicenseModel *string `pulumi:"licenseModel"`
	// A value that indicates whether to manage the master user password with AWS Secrets Manager.
	ManageMasterUserPassword *bool `pulumi:"manageMasterUserPassword"`
	// Contains the secret managed by RDS in AWS Secrets Manager for the master user password.
	MasterUserSecret *DBInstanceMasterUserSecret `pulumi:"masterUserSecret"`
	// The upper limit to which Amazon RDS can automatically scale the storage of the DB instance.
	MaxAllocatedStorage *int `pulumi:"maxAllocatedStorage"`
	// The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collecting Enhanced Monitoring metrics, specify 0. The default is 0.
	MonitoringInterval *int `pulumi:"monitoringInterval"`
	// The ARN for the IAM role that permits RDS to send enhanced monitoring metrics to Amazon CloudWatch Logs.
	MonitoringRoleArn *string `pulumi:"monitoringRoleArn"`
	// Specifies whether the database instance is a multiple Availability Zone deployment.
	MultiAZ *bool `pulumi:"multiAZ"`
	// The network type of the DB cluster.
	NetworkType *string `pulumi:"networkType"`
	// Indicates that the DB instance should be associated with the specified option group.
	OptionGroupName *string `pulumi:"optionGroupName"`
	// The AWS KMS key identifier for encryption of Performance Insights data. The KMS key ID is the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS encryption key.
	PerformanceInsightsKMSKeyId *string `pulumi:"performanceInsightsKMSKeyId"`
	// The amount of time, in days, to retain Performance Insights data. Valid values are 7 or 731 (2 years).
	PerformanceInsightsRetentionPeriod *int `pulumi:"performanceInsightsRetentionPeriod"`
	// The daily time range during which automated backups are created if automated backups are enabled, using the BackupRetentionPeriod parameter.
	PreferredBackupWindow *string `pulumi:"preferredBackupWindow"`
	// he weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
	PreferredMaintenanceWindow *string `pulumi:"preferredMaintenanceWindow"`
	// The number of CPU cores and the number of threads per core for the DB instance class of the DB instance.
	ProcessorFeatures []DBInstanceProcessorFeature `pulumi:"processorFeatures"`
	// A value that specifies the order in which an Aurora Replica is promoted to the primary instance after a failure of the existing primary instance.
	PromotionTier *int `pulumi:"promotionTier"`
	// Indicates whether the DB instance is an internet-facing instance. If you specify true, AWS CloudFormation creates an instance with a publicly resolvable DNS name, which resolves to a public IP address. If you specify false, AWS CloudFormation creates an internal instance with a DNS name that resolves to a private IP address.
	PubliclyAccessible *bool `pulumi:"publiclyAccessible"`
	// The open mode of an Oracle read replica. The default is open-read-only.
	ReplicaMode *string `pulumi:"replicaMode"`
	// Specifies the storage throughput for the DB instance.
	StorageThroughput *int `pulumi:"storageThroughput"`
	// Specifies the storage type to be associated with the DB instance.
	StorageType *string `pulumi:"storageType"`
	// Tags to assign to the DB instance.
	Tags []DBInstanceTag `pulumi:"tags"`
	// The ARN from the key store with which to associate the instance for TDE encryption.
	TdeCredentialArn *string `pulumi:"tdeCredentialArn"`
	// A value that indicates whether the DB instance class of the DB instance uses its default processor features.
	UseDefaultProcessorFeatures *bool `pulumi:"useDefaultProcessorFeatures"`
	// A list of the VPC security group IDs to assign to the DB instance. The list can include both the physical IDs of existing VPC security groups and references to AWS::EC2::SecurityGroup resources created in the template.
	VPCSecurityGroups []string `pulumi:"vPCSecurityGroups"`
}

func LookupDBInstanceOutput(ctx *pulumi.Context, args LookupDBInstanceOutputArgs, opts ...pulumi.InvokeOption) LookupDBInstanceResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupDBInstanceResult, error) {
			args := v.(LookupDBInstanceArgs)
			r, err := LookupDBInstance(ctx, &args, opts...)
			var s LookupDBInstanceResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupDBInstanceResultOutput)
}

type LookupDBInstanceOutputArgs struct {
	// A name for the DB instance. If you specify a name, AWS CloudFormation converts it to lowercase. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the DB instance.
	DBInstanceIdentifier pulumi.StringInput `pulumi:"dBInstanceIdentifier"`
}

func (LookupDBInstanceOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDBInstanceArgs)(nil)).Elem()
}

type LookupDBInstanceResultOutput struct{ *pulumi.OutputState }

func (LookupDBInstanceResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDBInstanceResult)(nil)).Elem()
}

func (o LookupDBInstanceResultOutput) ToLookupDBInstanceResultOutput() LookupDBInstanceResultOutput {
	return o
}

func (o LookupDBInstanceResultOutput) ToLookupDBInstanceResultOutputWithContext(ctx context.Context) LookupDBInstanceResultOutput {
	return o
}

// The amount of storage (in gigabytes) to be initially allocated for the database instance.
func (o LookupDBInstanceResultOutput) AllocatedStorage() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *string { return v.AllocatedStorage }).(pulumi.StringPtrOutput)
}

// A value that indicates whether major version upgrades are allowed. Changing this parameter doesn't result in an outage and the change is asynchronously applied as soon as possible.
func (o LookupDBInstanceResultOutput) AllowMajorVersionUpgrade() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *bool { return v.AllowMajorVersionUpgrade }).(pulumi.BoolPtrOutput)
}

// The AWS Identity and Access Management (IAM) roles associated with the DB instance.
func (o LookupDBInstanceResultOutput) AssociatedRoles() DBInstanceRoleArrayOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) []DBInstanceRole { return v.AssociatedRoles }).(DBInstanceRoleArrayOutput)
}

// A value that indicates whether minor engine upgrades are applied automatically to the DB instance during the maintenance window. By default, minor engine upgrades are applied automatically.
func (o LookupDBInstanceResultOutput) AutoMinorVersionUpgrade() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *bool { return v.AutoMinorVersionUpgrade }).(pulumi.BoolPtrOutput)
}

// The Availability Zone (AZ) where the database will be created. For information on AWS Regions and Availability Zones.
func (o LookupDBInstanceResultOutput) AvailabilityZone() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *string { return v.AvailabilityZone }).(pulumi.StringPtrOutput)
}

// The number of days for which automated backups are retained. Setting this parameter to a positive number enables backups. Setting this parameter to 0 disables automated backups.
func (o LookupDBInstanceResultOutput) BackupRetentionPeriod() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *int { return v.BackupRetentionPeriod }).(pulumi.IntPtrOutput)
}

// The identifier of the CA certificate for this DB instance.
func (o LookupDBInstanceResultOutput) CACertificateIdentifier() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *string { return v.CACertificateIdentifier }).(pulumi.StringPtrOutput)
}

// A value that indicates whether to copy tags from the DB instance to snapshots of the DB instance. By default, tags are not copied.
func (o LookupDBInstanceResultOutput) CopyTagsToSnapshot() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *bool { return v.CopyTagsToSnapshot }).(pulumi.BoolPtrOutput)
}

// The identifier for the RDS for MySQL Multi-AZ DB cluster snapshot to restore from. For more information on Multi-AZ DB clusters, see Multi-AZ deployments with two readable standby DB instances in the Amazon RDS User Guide .
//
// Constraints:
//   - Must match the identifier of an existing Multi-AZ DB cluster snapshot.
//   - Can't be specified when DBSnapshotIdentifier is specified.
//   - Must be specified when DBSnapshotIdentifier isn't specified.
//   - If you are restoring from a shared manual Multi-AZ DB cluster snapshot, the DBClusterSnapshotIdentifier must be the ARN of the shared snapshot.
//   - Can't be the identifier of an Aurora DB cluster snapshot.
//   - Can't be the identifier of an RDS for PostgreSQL Multi-AZ DB cluster snapshot.
func (o LookupDBInstanceResultOutput) DBClusterSnapshotIdentifier() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *string { return v.DBClusterSnapshotIdentifier }).(pulumi.StringPtrOutput)
}

// The Amazon Resource Name (ARN) for the DB instance.
func (o LookupDBInstanceResultOutput) DBInstanceArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *string { return v.DBInstanceArn }).(pulumi.StringPtrOutput)
}

// The compute and memory capacity of the DB instance, for example, db.m4.large. Not all DB instance classes are available in all AWS Regions, or for all database engines.
func (o LookupDBInstanceResultOutput) DBInstanceClass() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *string { return v.DBInstanceClass }).(pulumi.StringPtrOutput)
}

// The name of an existing DB parameter group or a reference to an AWS::RDS::DBParameterGroup resource created in the template.
func (o LookupDBInstanceResultOutput) DBParameterGroupName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *string { return v.DBParameterGroupName }).(pulumi.StringPtrOutput)
}

// A list of the DB security groups to assign to the DB instance. The list can include both the name of existing DB security groups or references to AWS::RDS::DBSecurityGroup resources created in the template.
func (o LookupDBInstanceResultOutput) DBSecurityGroups() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) []string { return v.DBSecurityGroups }).(pulumi.StringArrayOutput)
}

// The Oracle system ID (Oracle SID) for a container database (CDB). The Oracle SID is also the name of the CDB. This setting is valid for RDS Custom only.
func (o LookupDBInstanceResultOutput) DBSystemId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *string { return v.DBSystemId }).(pulumi.StringPtrOutput)
}

// The AWS Region-unique, immutable identifier for the DB instance. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.
func (o LookupDBInstanceResultOutput) DbiResourceId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *string { return v.DbiResourceId }).(pulumi.StringPtrOutput)
}

// A value that indicates whether to remove automated backups immediately after the DB instance is deleted. This parameter isn't case-sensitive. The default is to remove automated backups immediately after the DB instance is deleted.
func (o LookupDBInstanceResultOutput) DeleteAutomatedBackups() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *bool { return v.DeleteAutomatedBackups }).(pulumi.BoolPtrOutput)
}

// A value that indicates whether the DB instance has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is disabled.
func (o LookupDBInstanceResultOutput) DeletionProtection() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *bool { return v.DeletionProtection }).(pulumi.BoolPtrOutput)
}

// The Active Directory directory ID to create the DB instance in. Currently, only MySQL, Microsoft SQL Server, Oracle, and PostgreSQL DB instances can be created in an Active Directory Domain.
func (o LookupDBInstanceResultOutput) Domain() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *string { return v.Domain }).(pulumi.StringPtrOutput)
}

// Specify the name of the IAM role to be used when making API calls to the Directory Service.
func (o LookupDBInstanceResultOutput) DomainIAMRoleName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *string { return v.DomainIAMRoleName }).(pulumi.StringPtrOutput)
}

// The list of log types that need to be enabled for exporting to CloudWatch Logs. The values in the list depend on the DB engine being used.
func (o LookupDBInstanceResultOutput) EnableCloudwatchLogsExports() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) []string { return v.EnableCloudwatchLogsExports }).(pulumi.StringArrayOutput)
}

// A value that indicates whether to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts. By default, mapping is disabled.
func (o LookupDBInstanceResultOutput) EnableIAMDatabaseAuthentication() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *bool { return v.EnableIAMDatabaseAuthentication }).(pulumi.BoolPtrOutput)
}

// A value that indicates whether to enable Performance Insights for the DB instance.
func (o LookupDBInstanceResultOutput) EnablePerformanceInsights() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *bool { return v.EnablePerformanceInsights }).(pulumi.BoolPtrOutput)
}

// Specifies the connection endpoint.
func (o LookupDBInstanceResultOutput) Endpoint() DBInstanceEndpointPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *DBInstanceEndpoint { return v.Endpoint }).(DBInstanceEndpointPtrOutput)
}

// The name of the database engine that you want to use for this DB instance.
func (o LookupDBInstanceResultOutput) Engine() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *string { return v.Engine }).(pulumi.StringPtrOutput)
}

// The version number of the database engine to use.
func (o LookupDBInstanceResultOutput) EngineVersion() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *string { return v.EngineVersion }).(pulumi.StringPtrOutput)
}

// The number of I/O operations per second (IOPS) that the database provisions.
func (o LookupDBInstanceResultOutput) Iops() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *int { return v.Iops }).(pulumi.IntPtrOutput)
}

// License model information for this DB instance.
func (o LookupDBInstanceResultOutput) LicenseModel() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *string { return v.LicenseModel }).(pulumi.StringPtrOutput)
}

// A value that indicates whether to manage the master user password with AWS Secrets Manager.
func (o LookupDBInstanceResultOutput) ManageMasterUserPassword() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *bool { return v.ManageMasterUserPassword }).(pulumi.BoolPtrOutput)
}

// Contains the secret managed by RDS in AWS Secrets Manager for the master user password.
func (o LookupDBInstanceResultOutput) MasterUserSecret() DBInstanceMasterUserSecretPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *DBInstanceMasterUserSecret { return v.MasterUserSecret }).(DBInstanceMasterUserSecretPtrOutput)
}

// The upper limit to which Amazon RDS can automatically scale the storage of the DB instance.
func (o LookupDBInstanceResultOutput) MaxAllocatedStorage() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *int { return v.MaxAllocatedStorage }).(pulumi.IntPtrOutput)
}

// The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collecting Enhanced Monitoring metrics, specify 0. The default is 0.
func (o LookupDBInstanceResultOutput) MonitoringInterval() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *int { return v.MonitoringInterval }).(pulumi.IntPtrOutput)
}

// The ARN for the IAM role that permits RDS to send enhanced monitoring metrics to Amazon CloudWatch Logs.
func (o LookupDBInstanceResultOutput) MonitoringRoleArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *string { return v.MonitoringRoleArn }).(pulumi.StringPtrOutput)
}

// Specifies whether the database instance is a multiple Availability Zone deployment.
func (o LookupDBInstanceResultOutput) MultiAZ() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *bool { return v.MultiAZ }).(pulumi.BoolPtrOutput)
}

// The network type of the DB cluster.
func (o LookupDBInstanceResultOutput) NetworkType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *string { return v.NetworkType }).(pulumi.StringPtrOutput)
}

// Indicates that the DB instance should be associated with the specified option group.
func (o LookupDBInstanceResultOutput) OptionGroupName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *string { return v.OptionGroupName }).(pulumi.StringPtrOutput)
}

// The AWS KMS key identifier for encryption of Performance Insights data. The KMS key ID is the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS encryption key.
func (o LookupDBInstanceResultOutput) PerformanceInsightsKMSKeyId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *string { return v.PerformanceInsightsKMSKeyId }).(pulumi.StringPtrOutput)
}

// The amount of time, in days, to retain Performance Insights data. Valid values are 7 or 731 (2 years).
func (o LookupDBInstanceResultOutput) PerformanceInsightsRetentionPeriod() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *int { return v.PerformanceInsightsRetentionPeriod }).(pulumi.IntPtrOutput)
}

// The daily time range during which automated backups are created if automated backups are enabled, using the BackupRetentionPeriod parameter.
func (o LookupDBInstanceResultOutput) PreferredBackupWindow() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *string { return v.PreferredBackupWindow }).(pulumi.StringPtrOutput)
}

// he weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
func (o LookupDBInstanceResultOutput) PreferredMaintenanceWindow() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *string { return v.PreferredMaintenanceWindow }).(pulumi.StringPtrOutput)
}

// The number of CPU cores and the number of threads per core for the DB instance class of the DB instance.
func (o LookupDBInstanceResultOutput) ProcessorFeatures() DBInstanceProcessorFeatureArrayOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) []DBInstanceProcessorFeature { return v.ProcessorFeatures }).(DBInstanceProcessorFeatureArrayOutput)
}

// A value that specifies the order in which an Aurora Replica is promoted to the primary instance after a failure of the existing primary instance.
func (o LookupDBInstanceResultOutput) PromotionTier() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *int { return v.PromotionTier }).(pulumi.IntPtrOutput)
}

// Indicates whether the DB instance is an internet-facing instance. If you specify true, AWS CloudFormation creates an instance with a publicly resolvable DNS name, which resolves to a public IP address. If you specify false, AWS CloudFormation creates an internal instance with a DNS name that resolves to a private IP address.
func (o LookupDBInstanceResultOutput) PubliclyAccessible() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *bool { return v.PubliclyAccessible }).(pulumi.BoolPtrOutput)
}

// The open mode of an Oracle read replica. The default is open-read-only.
func (o LookupDBInstanceResultOutput) ReplicaMode() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *string { return v.ReplicaMode }).(pulumi.StringPtrOutput)
}

// Specifies the storage throughput for the DB instance.
func (o LookupDBInstanceResultOutput) StorageThroughput() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *int { return v.StorageThroughput }).(pulumi.IntPtrOutput)
}

// Specifies the storage type to be associated with the DB instance.
func (o LookupDBInstanceResultOutput) StorageType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *string { return v.StorageType }).(pulumi.StringPtrOutput)
}

// Tags to assign to the DB instance.
func (o LookupDBInstanceResultOutput) Tags() DBInstanceTagArrayOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) []DBInstanceTag { return v.Tags }).(DBInstanceTagArrayOutput)
}

// The ARN from the key store with which to associate the instance for TDE encryption.
func (o LookupDBInstanceResultOutput) TdeCredentialArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *string { return v.TdeCredentialArn }).(pulumi.StringPtrOutput)
}

// A value that indicates whether the DB instance class of the DB instance uses its default processor features.
func (o LookupDBInstanceResultOutput) UseDefaultProcessorFeatures() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) *bool { return v.UseDefaultProcessorFeatures }).(pulumi.BoolPtrOutput)
}

// A list of the VPC security group IDs to assign to the DB instance. The list can include both the physical IDs of existing VPC security groups and references to AWS::EC2::SecurityGroup resources created in the template.
func (o LookupDBInstanceResultOutput) VPCSecurityGroups() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupDBInstanceResult) []string { return v.VPCSecurityGroups }).(pulumi.StringArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupDBInstanceResultOutput{})
}
