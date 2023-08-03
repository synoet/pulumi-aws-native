// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package neptune

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::Neptune::DBInstance
//
// Deprecated: DbInstance is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type DbInstance struct {
	pulumi.CustomResourceState

	AllowMajorVersionUpgrade   pulumi.BoolPtrOutput     `pulumi:"allowMajorVersionUpgrade"`
	AutoMinorVersionUpgrade    pulumi.BoolPtrOutput     `pulumi:"autoMinorVersionUpgrade"`
	AvailabilityZone           pulumi.StringPtrOutput   `pulumi:"availabilityZone"`
	DbClusterIdentifier        pulumi.StringPtrOutput   `pulumi:"dbClusterIdentifier"`
	DbInstanceClass            pulumi.StringOutput      `pulumi:"dbInstanceClass"`
	DbInstanceIdentifier       pulumi.StringPtrOutput   `pulumi:"dbInstanceIdentifier"`
	DbParameterGroupName       pulumi.StringPtrOutput   `pulumi:"dbParameterGroupName"`
	DbSnapshotIdentifier       pulumi.StringPtrOutput   `pulumi:"dbSnapshotIdentifier"`
	DbSubnetGroupName          pulumi.StringPtrOutput   `pulumi:"dbSubnetGroupName"`
	Endpoint                   pulumi.StringOutput      `pulumi:"endpoint"`
	Port                       pulumi.StringOutput      `pulumi:"port"`
	PreferredMaintenanceWindow pulumi.StringPtrOutput   `pulumi:"preferredMaintenanceWindow"`
	Tags                       DbInstanceTagArrayOutput `pulumi:"tags"`
}

// NewDbInstance registers a new resource with the given unique name, arguments, and options.
func NewDbInstance(ctx *pulumi.Context,
	name string, args *DbInstanceArgs, opts ...pulumi.ResourceOption) (*DbInstance, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DbInstanceClass == nil {
		return nil, errors.New("invalid value for required argument 'DbInstanceClass'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource DbInstance
	err := ctx.RegisterResource("aws-native:neptune:DbInstance", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDbInstance gets an existing DbInstance resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDbInstance(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DbInstanceState, opts ...pulumi.ResourceOption) (*DbInstance, error) {
	var resource DbInstance
	err := ctx.ReadResource("aws-native:neptune:DbInstance", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DbInstance resources.
type dbInstanceState struct {
}

type DbInstanceState struct {
}

func (DbInstanceState) ElementType() reflect.Type {
	return reflect.TypeOf((*dbInstanceState)(nil)).Elem()
}

type dbInstanceArgs struct {
	AllowMajorVersionUpgrade   *bool           `pulumi:"allowMajorVersionUpgrade"`
	AutoMinorVersionUpgrade    *bool           `pulumi:"autoMinorVersionUpgrade"`
	AvailabilityZone           *string         `pulumi:"availabilityZone"`
	DbClusterIdentifier        *string         `pulumi:"dbClusterIdentifier"`
	DbInstanceClass            string          `pulumi:"dbInstanceClass"`
	DbInstanceIdentifier       *string         `pulumi:"dbInstanceIdentifier"`
	DbParameterGroupName       *string         `pulumi:"dbParameterGroupName"`
	DbSnapshotIdentifier       *string         `pulumi:"dbSnapshotIdentifier"`
	DbSubnetGroupName          *string         `pulumi:"dbSubnetGroupName"`
	PreferredMaintenanceWindow *string         `pulumi:"preferredMaintenanceWindow"`
	Tags                       []DbInstanceTag `pulumi:"tags"`
}

// The set of arguments for constructing a DbInstance resource.
type DbInstanceArgs struct {
	AllowMajorVersionUpgrade   pulumi.BoolPtrInput
	AutoMinorVersionUpgrade    pulumi.BoolPtrInput
	AvailabilityZone           pulumi.StringPtrInput
	DbClusterIdentifier        pulumi.StringPtrInput
	DbInstanceClass            pulumi.StringInput
	DbInstanceIdentifier       pulumi.StringPtrInput
	DbParameterGroupName       pulumi.StringPtrInput
	DbSnapshotIdentifier       pulumi.StringPtrInput
	DbSubnetGroupName          pulumi.StringPtrInput
	PreferredMaintenanceWindow pulumi.StringPtrInput
	Tags                       DbInstanceTagArrayInput
}

func (DbInstanceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*dbInstanceArgs)(nil)).Elem()
}

type DbInstanceInput interface {
	pulumi.Input

	ToDbInstanceOutput() DbInstanceOutput
	ToDbInstanceOutputWithContext(ctx context.Context) DbInstanceOutput
}

func (*DbInstance) ElementType() reflect.Type {
	return reflect.TypeOf((**DbInstance)(nil)).Elem()
}

func (i *DbInstance) ToDbInstanceOutput() DbInstanceOutput {
	return i.ToDbInstanceOutputWithContext(context.Background())
}

func (i *DbInstance) ToDbInstanceOutputWithContext(ctx context.Context) DbInstanceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DbInstanceOutput)
}

type DbInstanceOutput struct{ *pulumi.OutputState }

func (DbInstanceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DbInstance)(nil)).Elem()
}

func (o DbInstanceOutput) ToDbInstanceOutput() DbInstanceOutput {
	return o
}

func (o DbInstanceOutput) ToDbInstanceOutputWithContext(ctx context.Context) DbInstanceOutput {
	return o
}

func (o DbInstanceOutput) AllowMajorVersionUpgrade() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *DbInstance) pulumi.BoolPtrOutput { return v.AllowMajorVersionUpgrade }).(pulumi.BoolPtrOutput)
}

func (o DbInstanceOutput) AutoMinorVersionUpgrade() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *DbInstance) pulumi.BoolPtrOutput { return v.AutoMinorVersionUpgrade }).(pulumi.BoolPtrOutput)
}

func (o DbInstanceOutput) AvailabilityZone() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DbInstance) pulumi.StringPtrOutput { return v.AvailabilityZone }).(pulumi.StringPtrOutput)
}

func (o DbInstanceOutput) DbClusterIdentifier() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DbInstance) pulumi.StringPtrOutput { return v.DbClusterIdentifier }).(pulumi.StringPtrOutput)
}

func (o DbInstanceOutput) DbInstanceClass() pulumi.StringOutput {
	return o.ApplyT(func(v *DbInstance) pulumi.StringOutput { return v.DbInstanceClass }).(pulumi.StringOutput)
}

func (o DbInstanceOutput) DbInstanceIdentifier() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DbInstance) pulumi.StringPtrOutput { return v.DbInstanceIdentifier }).(pulumi.StringPtrOutput)
}

func (o DbInstanceOutput) DbParameterGroupName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DbInstance) pulumi.StringPtrOutput { return v.DbParameterGroupName }).(pulumi.StringPtrOutput)
}

func (o DbInstanceOutput) DbSnapshotIdentifier() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DbInstance) pulumi.StringPtrOutput { return v.DbSnapshotIdentifier }).(pulumi.StringPtrOutput)
}

func (o DbInstanceOutput) DbSubnetGroupName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DbInstance) pulumi.StringPtrOutput { return v.DbSubnetGroupName }).(pulumi.StringPtrOutput)
}

func (o DbInstanceOutput) Endpoint() pulumi.StringOutput {
	return o.ApplyT(func(v *DbInstance) pulumi.StringOutput { return v.Endpoint }).(pulumi.StringOutput)
}

func (o DbInstanceOutput) Port() pulumi.StringOutput {
	return o.ApplyT(func(v *DbInstance) pulumi.StringOutput { return v.Port }).(pulumi.StringOutput)
}

func (o DbInstanceOutput) PreferredMaintenanceWindow() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DbInstance) pulumi.StringPtrOutput { return v.PreferredMaintenanceWindow }).(pulumi.StringPtrOutput)
}

func (o DbInstanceOutput) Tags() DbInstanceTagArrayOutput {
	return o.ApplyT(func(v *DbInstance) DbInstanceTagArrayOutput { return v.Tags }).(DbInstanceTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DbInstanceInput)(nil)).Elem(), &DbInstance{})
	pulumi.RegisterOutputType(DbInstanceOutput{})
}
